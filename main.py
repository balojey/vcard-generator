from datetime import datetime
from flask import (
    Flask,
    flash,
    url_for,
    redirect,
    render_template,
    send_file,
    send_from_directory,
)
from utils import add_prefix, add_suffix
from flask import Flask, render_template, request
from flask_htmx import HTMX, make_response
import os
import pandas as pd
from vcf_creator.vcf import vcard_formatter, vcard_generator


app = Flask(__name__)
htmx = HTMX(app)
app.secret_key = "8135213608"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if htmx:
        prefix = request.form["prefix"]
        suffix = request.form["suffix"]
        file = request.files["excel_sheet"]
        df = pd.read_excel(file)

        # Check if the sheet is empty
        if df.empty:
            flash("The excel sheet is empty!")
            return redirect(url_for("index"))

        # Check if the sheet has both name and phone number columns
        headers: str = df.columns.values
        if "PHONE" not in headers or "PHONE" not in headers:
            flash("The sheet does not have 'NAME' and 'PHONE' headers!")
            return redirect(url_for("index"))

        print(df)

        # Check for duplicate phone numbers
        # df: pd.DataFrame = df.drop_duplicates(subset="PHONE", keep="first")

        # Add suffix to names if suffix is not ' ' or none
        if suffix != " " or suffix != None:
            df["NAME"] = df["NAME"].apply(add_suffix, args=(suffix,))

        # Add prefix to names if prefix is not ' ' or none
        if prefix != " " or prefix != None:
            df["NAME"] = df["NAME"].apply(add_prefix, args=(prefix,))

        # Convert dataframe to csv
        csv_output_file: str = (
            "./contact_csv_files/output-" + str(datetime.now().utcnow()) + ".csv"
        )
        df.to_csv(csv_output_file, index=False)

        # Generate vcf string
        ret_str: str = vcard_generator(csv_output_file)

        # Store vcf string in a .vcf file
        vcf_file: str = (
            "./contact_vcf_files/output-" + str(datetime.now().utcnow()) + ".vcf"
        )
        with open(vcf_file, "w") as f:
            f.write(ret_str)

        return render_template("partials/download.html", vcf_file=vcf_file)


@app.route("/download/<path:filename>")
def download(filename: str):
    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)

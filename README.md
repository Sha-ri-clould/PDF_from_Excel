# What is this project?
This is an app that creates PDF invoices out of Excel files.

## Features
#### Reads .xlsx invoices from the folder.
#### Parses invoice number and date from the file name.
#### Automatically formats:Table headers, Total invoice sum.
#### Adds branding: company name + logo.
#### Saves generated PDFs.

## How to use?
#### Upload Excel files in invoices/ folder.
#### Install pathlib, fpdf, glob, pandas libraries.
#### Ensure each filename is formatted like: invoiceNumber-date.xlsx
#### Add company name and logo path.
#### Find generated PDFs in the invoices_PDF/ directory.

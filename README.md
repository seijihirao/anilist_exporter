# Anilist exporter

Simple anilist util to export its data to a given format.

## Using

Run in your shell

```bash
$ python main.py -u myuser -e myexporter > outputfile
```

With
 * myuser - being your anilist user
 * myexporter - the exporter filename
 * outputfile - the file to write to

E.g.

```bash
$ python main.py -u seijihirao -e letterboxd > output.csv
```

## Creating exporters

To create a new exporter, just create a new file inside the dir [lib/exporters](./lib/exporters/).

This file must contain an `Exporter` class with the functions `export_meta()` (to return header line) and `export_media(media)` (to return each line),
see [letterboxd file](./lib/exporters/letterboxd.py)

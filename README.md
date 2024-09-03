# Tex Match - An Image Comparison Tool

## Overview

This project provides tools to compare two images using a similarity metric and aggregate the results for further analysis. The tools are designed to work with `.dds` texture files but can be extended to support other image formats.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Features

- **Image Inspector**: Compares two images and calculates similarity using SSIM and created a delta image.
- **Observation Saver**: Stores comparison results, including images and metrics, in a structured directory format.
- **Aggregate Data**: Filters and aggregates comparison results based on a user-defined similarity threshold.

## Installation
Install uv and sync with the provided pyproject.toml:
```bash
pip install uv
uv init
source .venv/bin/activate
uv sync

```
Or via pip and requirements.txt
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
If it take along time for opencv to install, try updating pip, setuptools and wheel:
```bash
pip install --upgrade pip setuptools wheel
```

### Prerequisites

- **Python Version**: Python 3.12+
- **Other Tools**: `pip`, `virtualenv`

## Usage
### Makefile commands
To simplify running the image comparison and aggregation tasks, the provided Makefile can be used.

#### Run Predefined Examples:
```bash
make example1
... 
make example4
```
#### Run Custom Image Comparison
Compare custom images located in resources/DDSTextures/.
```bash
make run-custom IMG1=<image1> IMG2=<image2>
```
#### Aggregate Data
Aggregate comparison data with a similarity threshold.
```bash
make agg TH=<threshold>
```
#### Clean Output
Remove the observations directory.
```bash
make clean
```
#### Help:
Show available commands.
```bash
make help
```

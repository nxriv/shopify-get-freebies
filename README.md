# Shopify Freebie Grabber

> Simple script to allow you to input a shopify URL, and output a link to add all the free items from the store to your cart.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Introduction

This Python project uses the request library. It will grab the products.json pages and read from the data.
Please NOTE: This is not supported by all stores. Some stores also do not want users to purchase these free items. Utilize this responsibly, and where you have implicit permission ONLY.

### Features

- Returns HTTP response codes upon failure.
- Returns an add all cart link with product IDs upon success.
- Prepends `https://` if missing.

## Getting Started

`py free.py`

### Prerequisites

requests library.


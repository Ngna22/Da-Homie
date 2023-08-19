#!/usr/bin/env bash

while true
  do
    python3 main.py
    git pull --rebase=true
  done


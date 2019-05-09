#!/usr/bin/env bash
# Bash script for iterating through host arguments

for host in "$@"
do
    scp "$SCP_FILE" ubuntu@"$host":~/
done

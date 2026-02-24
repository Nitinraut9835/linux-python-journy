#!/bin/bash

# Nginx Log Monitoring Script
# Author: Nitin
# Description:
#   - Counts total requests for today
#   - Counts 404 errors
#   - Calculates 404 error percentage
#   - Generates formatted daily report
#
# Usage:
#   ./monitor.sh
LOG="/var/log/nginx/access.log"
TODAY=$(date '+%d/%b/%Y')

# Check if log exists
if [ ! -f "$LOG" ]; then
    echo "Log file not found!"
    exit 1
fi

TOTAL=$(grep "$TODAY" "$LOG" | wc -l)
ERRORS=$(grep "$TODAY" "$LOG" | awk '$9 == 404' | wc -l)

if [ "$TOTAL" -eq 0 ]; then
    PERCENT=0
else
    PERCENT=$((ERRORS * 100 / TOTAL))
fi

echo "=============================="
echo " NGINX DAILY REPORT"
echo " Date: $TODAY"
echo "------------------------------"
echo " Total Requests: $TOTAL"
echo " 404 Errors: $ERRORS"
echo " 404 Percentage: $PERCENT%"
echo "=============================="

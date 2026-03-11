#!/bin/bash

echo "Top IP addresses:"
docker logs nginx_server | awk '{print $1}' | sort | uniq -c | sort -nr | head

echo ""
echo "Most requested endpoints:"
docker logs nginx_server | awk '{print $7}' | sort | uniq -c | sort -nr | head

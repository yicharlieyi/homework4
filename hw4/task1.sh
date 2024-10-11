#!/bin/bash
pid=$(pgrep -f "infinite.sh")

if [ -n "$pid" ]; then
  kill -9 $pid
  echo "Killed infinite.sh. PID: $pid"
else
  echo "infinite.sh is not currently running"
fi

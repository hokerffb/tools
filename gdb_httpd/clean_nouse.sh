cd logs
grep -rn "exited normally" *|awk '{split($0, a, ":"); print a[1];}'|xargs rm -f
grep -rn "Broken pipe" *|awk '{split($0, a, ":"); print a[1];}'|xargs rm -f

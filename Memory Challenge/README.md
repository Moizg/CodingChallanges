# The Actual Memory Size of Your USB Flash Drive

Create a function that takes the memory size (ms) as an argument and returns the actual memory size.

## Examples

```
actualMemorySize("32GB")
output = "29.76GB"

actualMemorySize("2GB")
output = "1.86GB"

actualMemorySize("512MB")
output = "476MB"
```

## Notes

- The actual storage loss on a USB device is 7% of the overall memory size!
- If the actual memory size was greater than 1 GB, round your result to two decimal places.
- If the memory size after adjustment is smaller then 1 GB, return the result in MB.
- For the purposes of this challenge, there are 1000 MB in a Gigabyte.
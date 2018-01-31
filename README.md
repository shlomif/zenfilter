This small script filters long STDIN output, performing several functions
to keep track of the important parts and progresses, which will be hard to
do with a shell script.

It is useful for filtering the output of verbose
[Travis-CI](https://travis-ci.org/) commands, but may be useful in other
contexts where there is a limit to the amount of kept output.

All arguments are optional:

* `--count-step=n`: displays `COUNT <tab> <step>` every n lines.
* `--last=n`: displays the last n lines prefixed with "LAST\t"
* `--filter=<regex pattern>`: displays matching lines with a "FOUND\t" prefix.
* `--suppress-last-on=<regex>`: suppress the last lines if their concatenated output matches the regex.

Examples:

```sh
python zenfilter.py --count-step=10 --last=200 --filter="\d+"
python zenfilter.py --last=20
python zenfilter.py --last=25 --count-step=15
```

A use case scenario:

```sh
make 2>&1 | python zenfilter.py [args]
```

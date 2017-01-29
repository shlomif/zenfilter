This small script is used to filter TravisCI output.


All arguments are optional: 

--count-step=n: displays "COUNT <tab> <step>" every n lines.
--last=n: displays the last n lines prefixed with "LAST\t"
--filter=<regex pattern>: displays matching lines with a "FOUND\t" prefix.

python zenfilter.py --count-step=10 --last=200 --filter="\d+"
python zenfilter.py --last=20
python zenfilter.py --last=25 --count-step=15

# "make | python zenfilter.py [args]"


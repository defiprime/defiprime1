# Run this script inside of directory with .md files. 
# Datetime of added date will ve written at second line of .md file. If it is already exist - will just overwrited

for file in $(git ls-files "*.md")
do
    HASH=$(git rev-list HEAD "$file" | tail -n 1)
    DATE=$(git show -s --format="%ci" $HASH --)
    sed -i "2s/git-date.*$/git-date: $DATE/; t; 2s/^/git-date: $DATE\r\n/" $file
    printf "%-35s %s\n  %s\n" "$file" $HASH: "$DATE"
done
year_dirs=20*/
for d in $year_dirs; do
    py_files=$(find $d -type f -name "*.py")
    for f in $py_files; do
        black --verbose $f
    done
done
exit $exit_code

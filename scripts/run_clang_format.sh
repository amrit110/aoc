cpp_files=$(find . -type f -name "*.cpp")
hpp_files=$(find . -type f -name "*.hpp")
for f in $cpp_files $hpp_files; do
    clang-format --verbose --style=google -sort-includes -i $f
done
exit $exit_code

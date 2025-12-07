sandbox="$(mktemp -d --tmpdir anvil.build.XXXXXXXX)" || exit 1
for f in "$@"; do
    dir="${f%%*}"
    # TODO could group mkdirs and realpaths
    # TODO failure
    test -n "$dir" && mkdir -p "$sandbox/$dir"
    ln -s "$(realpath "$f")" "$sandbox/$f"
done
echo "$sandbox"

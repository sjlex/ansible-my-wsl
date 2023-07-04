# This function is typically bound to Alt-L, it is used to list the contents
# of the directory under the cursor.

function user_list_current_token -d "List contents of token under the cursor if it is a directory, otherwise list the contents of the current directory"
  set -f val (commandline -t)

  printf "\n"

  if test -d $val
    la $val
  else
    set -l dir (dirname -- $val)
    if test $dir != . -a -d $dir
      la $dir
    else
      la
    end
  end

  string repeat -N \n --count=(math (count (fish_prompt)) - 1)

  commandline -f repaint
end

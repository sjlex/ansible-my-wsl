function user_fzf_select_z
  set -f query (commandline)

  if test -n $query
    set fzf_flags --query "$query"
  end

  z -l | sort -rn | cut -c 12- | fzf $FZF_DEFAULT_OPTS $fzf_flags | read line

  if test $line
    cd $line
    commandline -f repaint
  end
end

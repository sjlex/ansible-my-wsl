function fish_user_key_bindings
  # ls
  bind \el 'user_list_current_token'

  # fzf
  bind \cf '__fzf_find_file'
  bind \cr '__fzf_reverse_isearch'
  bind \ce 'user_fzf_select_z'
  bind \ct '__fzf_cd'
  bind \ch '__fzf_cd --hidden'
end

print("hello worlds")

# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git push
# fatal: No configured push destination.
# Either specify the URL from the command-line or configure a remote repository using

#     git remote add <name> <url>

# and then push using the remote name

#     git push <name>

# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git push hello.html
# fatal: The current branch main has no upstream branch.
# To push the current branch and set the remote as upstream, use

#     git push --set-upstream hello.html main

# To have this happen automatically for branches without a tracking
# upstream, see 'push.autoSetupRemote' in 'git help config'.

# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git push
# fatal: No configured push destination.
# Either specify the URL from the command-line or configure a remote repository using

#     git remote add <name> <url>

# and then push using the remote name

#     git push <name>

# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git add hello.html
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git commit -m "new file added hello.html"
# [main be148b7] new file added hello.html
#  1 file changed, 17 insertions(+), 1 deletion(-)
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git status
# On branch main
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         hello.py
#         python/

# nothing added to commit but untracked files present (use "git add" to track)
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git add hello.py
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git add python
# error: 'python/' does not have a commit checked out
# fatal: adding files failed
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git add python/
# error: 'python/' does not have a commit checked out
# fatal: adding files failed
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git statusOn branch main
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   hello.py

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         python/

# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git status
# On branch main
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   hello.py

# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git commit -m "new file added hello.html and hello.py"
# [main 6a07adb] new file added hello.html and hello.py
#  1 file changed, 2 insertions(+)
#  create mode 100644 hello.py
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git push
# fatal: No configured push destination.
# Either specify the URL from the command-line or configure a remote repository using

#     git remote add <name> <url>

# and then push using the remote name

#     git push <name>

# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git remote add origin https://github.com/deepthikbs/python.git
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git pushfatal: The current branch main has no upstream branch.
# To push the current branch and set the remote as upstream, use

#     git push --set-upstream origin main

# To have this happen automatically for branches without a tracking
# upstream, see 'push.autoSetupRemote' in 'git help config'.

# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 %     git push --set-upstream origin main
# Username for 'https://github.com': kbs_deepthi 
# Password for 'https://kbs_deepthi@github.com': 
# remote: Support for password authentication was removed on August 13, 2021.
# remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
# fatal: Authentication failed for 'https://github.com/deepthikbs/python.git/'
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 %     git push --set-upstream origin main
# Username for 'https://github.com': kbsdeepthi
# Password for 'https://kbsdeepthi@github.com': 
# remote: Support for password authentication was removed on August 13, 2021.
# remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
# fatal: Authentication failed for 'https://github.com/deepthikbs/python.git/'
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 %     git push --set-upstream origin main
# Username for 'https://github.com': deepthikbs
# Password for 'https://deepthikbs@github.com': 
# remote: Support for password authentication was removed on August 13, 2021.
# remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
# fatal: Authentication failed for 'https://github.com/deepthikbs/python.git/'
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 %     git push --set-upstream origin main
# Username for 'https://github.com': deepthikbs
# Password for 'https://deepthikbs@github.com': 
# remote: Support for password authentication was removed on August 13, 2021.
# remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
# fatal: Authentication failed for 'https://github.com/deepthikbs/python.git/'
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % git remote set-url origin https://<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>@github.com/<deepthikbs>/<python>.git        

# zsh: no such file or directory: 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
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 %     git push --set-upstream origin mainUsername for 'https://github.com': deepthikbs
# Password for 'https://deepthikbs@github.com': 
# remote: Support for password authentication was removed on August 13, 2021.
# remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
# fatal: Authentication failed for 'https://github.com/deepthikbs/python.git/'
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 %     git push --set-upstream origin main
# Username for 'https://github.com': deepthikbs
# Password for 'https://deepthikbs@github.com': 
# Enumerating objects: 9, done.
# Counting objects: 100% (9/9), done.
# Delta compression using up to 8 threads
# Compressing objects: 100% (6/6), done.
# Writing objects: 100% (9/9), 1.09 KiB | 1.09 MiB/s, done.
# Total 9 (delta 1), reused 0 (delta 0), pack-reused 0
# remote: Resolving deltas: 100% (1/1), done.
# To https://github.com/deepthikbs/python.git
#  * [new branch]      main -> main
# branch 'main' set up to track 'origin/main'.
# (base) deepthikuntamukkala@MacBook-Air21 python-cs50 % 
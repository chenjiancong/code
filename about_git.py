#Filename: about_git.txt
#-*- coding:utf-8 -*-
#关于git的相关命令

#生成SSH-KEYGEN
ssh-keygen -t rsa -C "youremail"
id_rsa.pub 是公钥

#开始配置信息
git config --global user.name "name"
git config --global user.email "email@"
#打开色彩显示
git config --global color.ui true

git init   #初始化git
git add file   #加入暂存区
git commit -m "tag or something"   #暂存区文件提交
git status   #查看git状态

#查看log
git reflog    #查看commit_id
git log --pretty=oneline

#撤销
git checkout -- file    #撤销工作区文件修改(未提交未加入暂存区)
git reset HEAD file    #已加入暂存区未提交，然后再执行 checkout 命令
git reset --hard HEAD^(commit_id)   #退回之前版本

#远程相关命令
git remote add origin git@github.com:name/project.git               #添加远程主机
git clone git@github.com:name.com/project.git   #克隆项目
git pull origin <remote> <remote_branch_name>:<local_branch_name>   #取回远程的某个分支到本地并合并
                                                                    #相当先执行fetch,再执行merge
#取远程分支作为本地新分支
git checkout -b newBranch origin/master

git fetch orign branch_name                                         #将远程分支取回到本地
git push origin <remote> <local_branch_name>:<remote_branch_name>   #推送到远程分支
git branch      #查看本地分支
git branch -r   #查看远程分支
git checkout branch_name   #切换到分支
git branch branch_name   #建立分支
git fetch <remote>
git merge branch_name   #合并分支(首先要切换到待合并分支上，然后再执行要合并的分支
    ex：要将dev 与 master 合并，需先checkout 到 master 再执行 merge dev)
git branch -d branch_name   #删除分支
git push origin :branch_name  #删除远程分支(推送一个空分支)

#  git 每次输入密码
每次push  的时候，都要输入用户名和密码
原因是使用了https方式 push
在termail里边 输入  git remote -v
可以看到形如一下的返回结果
origin https://github.com/yourname/demo.git (fetch)
origin https://github.com/yourname/demo.git (push)
下面把它换成ssh方式的。
1. git remote rm origin
2. git remote add origin git@github.com:yourname/demo.git
3. git push origin

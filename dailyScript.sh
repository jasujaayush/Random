#!/bin/bash -e
cd /home/ayush/Downloads/vision
sed -i -e 's/Vision/vision/g' /home/ayush/Downloads/vision/README.md 
commit_message="From Daily Git Push Script"
git add README.md
git commit -m "$commit_message"
git push https://<Username>:<Password>@github.com/Username/repo.git


sed -i -e 's/vision/Vision/g' /home/ayush/Downloads/vision/README.md
commit_message="From Daily Git Push Script"
git add README.md
git commit -m "$commit_message"
git push https://<Username>:<Password>@github.com/Username/repo.git

# to store the credentials one time
git config --global credential.helper store

echo ""
echo "Name of the repository: "
read repository
echo ""
echo "Adding remotes repositories"
echo ""
echo "Add gitlab"
echo ""
git remote add gitlab https://gitlab.com/gautier_debaudre/$repository.git
echo "Add github"
echo ""
git remote add github https://github.com/French-isotope/$repository.git
# Creating branch
echo "Create branch 'main'"
echo ""
git branch main
echo "Checkout branch 'main'"
echo ""
git checkout main
echo ""
git push -u github main
echo ""
git push -u gitlab main
echo ""


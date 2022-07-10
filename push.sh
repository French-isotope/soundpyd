# to store the credentials one time
# git config --global credential.helper store
# then 
# git pull gitlab main
# git pull github main

git add .
echo "Enter commit message"

read varname

git commit -m "$(echo $varname)"

echo ""
echo ""
echo "- push to gitlab -"
echo ""

git config --global --replace-all user.email "gautier.debaudre@gmail.com"
git config --global --replace-all user.name "GDE"
git config --replace-all user.email "gautier.debaudre@gmail.com"
git config --replace-all user.name "GDE"

git push -u gitlab --all

echo ""
echo ""
echo "- push to github -"
echo ""

git config --global --replace-all user.email "French.isotope@gmail.com"
git config --global --replace-all user.name "French-isotope"
git config --replace-all user.email "French.isotope@gmail.com"
git config --replace-all user.name "French-isotope"

git push -u github --all

echo ""


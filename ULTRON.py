#!/bin/bash


_python_() {
    python3${pVer%.*} -c "$1"
}

_ULTRONBOT_MAIN() {
    $(_python_ 'from git import Repo
import sys

_UPSTREAM_ = "https://github.com/LEGENDXTHANOS/ULTRONBOT"
_BRANCH_ = "master"

repo = Repo.init()
origin = repo.create_remote("temponame", _UPSTREAM_)
origin.fetch()
repo.create_head(_BRANCH_, origin.refs[_BRANCH_])
repo.heads[_BRANCH_].checkout(True) ')
}

_ultron_repo () {
    local hrepo
    hrepo=`echo "aHR0cHM6Ly9naXRodWIuY29tL0xFR0VORFhUSEFOT1MvVUxUUk9OVVNFUkJPVA==" | base64 -d`
    echo "$rlink"
}

_ultron_zip () {
    echo "aHR0cHM6Ly9naXRodWIuY29tL0xFR0VORFhUSEFOT1MvVUxUUk9OVVNFUkJPVC9hcmNoaXZlL21hc3Rlci56aXA=" | base64 -d
}

_ULTRONBOT_PLUG() {
    local hrepo=$(_ultron_repo)
    $(_python_ 'from git import Repo
import sys
_UPSTREAM_ = "'$hrepo'"
_BRANCH_ = "master"
repo = Repo.init()
origin = repo.create_remote("temponame", _UPSTREAM_)
origin.fetch()
repo.create_head(_BRANCH_, origin.refs[_BRANCH_])
repo.heads[_BRANCH_].checkout(True) ')
}

_starter () {
    local ultronpath
    ultronpath="ULTRONUSERBOT.zip"
    echo "╔════❰𓆩༒𝕾𝖙𝖆𝖗𝖙𝖎𝖓𝖌 𝖀𝖑𝖙𝖗𝖔𝖓𝕭𝖔𝖙𓆩༒❱═❍⊱❁"
    echo "║╭━━━━━━━━━━━━━━━➣"
    echo "║┣⪼𓆩༒ 𝖀𝖑𝖙𝖗𝖔𝖓𝕭𝖔𝖙 𝖀𝖑𝖙𝖗𝖆 𝕻𝖔𝖜𝖊𝖗𝕱𝖚𝖑𝖑༒𓆪"
    echo "║┣⪼𓆩༒𝕺𝖜𝖓𝖊𝖗 𝕺𝖋 𝖀𝖑𝖙𝖗𝖔𝖓=𝕷𝖊𝖌𝖊𝖓𝖉𝖃 𝕿𝖍𝖆𝖓𝖔𝖘༒𓆪"
    echo "║╰━━━━━━━━━━━━━━━➣"
    echo "╚══════════════════❍⊱❁۪۪"
    wget -q $(_ultron_zip) -O "$ultronpath"
    ULTRONPATH=$(zipinfo -1 "$ultronpath" | grep -v "/.");
    unzip -qq "$ultronpath"
    rm -rf "$ultronpath"
    # _ULTRONBOT_MAIN
    cd $ULTRONPATH
    # _ULTRONBOT_PLUG
    python3 ../setup/updater.py ../requirements.txt requirements.txt
    echo "╭━━━━━━━━━━━━━━━➣"
    echo "║┣⪼𝕷𝖔𝖆𝖉𝖎𝖓𝖌. 𝖀𝖑𝖙𝖗𝖔𝖓 𝕻𝖔𝖜𝖊𝖗𝕱𝖚𝖑𝖑 𝕽𝖔𝕭𝖔𝖔𝖙"
    echo "╰━━━━━━━━━━━━━━━➣"
    python3 -m UltronBot
}

_starter

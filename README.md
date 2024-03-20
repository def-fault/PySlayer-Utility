# PySlayer-Utility
Utilities developed for more features of mirusu400/PySlayer



> lang_kor

hsencrypt.py : 윈드슬레이어 클라이언트 파일을 재암호화하는 파일

(이미지 외 hs* 파일은 ValidationCheck.dll의 패치가 필요함)


ValidationCheck.dll : 파일 변조 시 SHA-1 검증 우회를 위해 수정된 DLL


patcher.py & gameserver.py : 패쳐에서 멀티플레이어를 위한 IP 입력 파트 수정

(mirusu400/PySlayer 최신버전에서 작동하지 않을 수 있음)


> lang_eng

hsencrypt.py : Files that re-encrypt Windslayer client files

(Non-image hs* files require patching from ValidationCheck.dll)


ValidationCheck.dll : Modify DLL for SHA-1 verification bypass when modulating files


patcher.py & gameserver.py : Modifying IP Input Part for Multiplayer in Patcher

(mirusu400/PySlayer may not work with the latest version)


> sound error

latest clients offered by def fault(self):

It may have some sound error.


2010.11.09 09:41:00.881 - ./Sound/skill_ice.wav invalid File. 6 C:\Program Files\Yahoo!Games\WindSlayer
2010.11.09 09:41:01.494 - ./Sound/ice_bolt.wav invalid File. 6 C:\Program Files\Yahoo!Games\WindSlayer


It's an error where certain skills sound different skills.

you must download these files and drag to sound folder.

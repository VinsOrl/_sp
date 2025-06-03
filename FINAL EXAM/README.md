# 系統程式設計 期末
# 資工二 111210556 林新興

## 習題一

[HW1](https://github.com/VinsOrl/_sp/tree/main/HW1)

參考同學，使用ChatGPT調試問題
```
// DOWHILE = do STMT while (E);
void DOWHILE() {
  int doBegin = nextLabel();
  int doEnd = nextLabel();
  emit("(L%d)\n", doBegin);
  skip("do");
  STMT();
  skip("while");
  skip("(");
  int e = E();
  skip(")");
  skip(";");
  emit("if t%d goto L%d\n", e, doBegin);
  emit("(L%d)\n", doEnd);
}

```

---

## 習題二

[HW2](https://github.com/VinsOrl/_sp/tree/main/HW2)
[result](https://github.com/VinsOrl/_sp/blob/main/HW2/00d-c4symdump/test/power2.md)

參考同學，使用ChatGPT調試問題和老師的資料
```
## C4 Output

1> ENT 0
2> IMM -1127669744
3> PSH
4> IMM 3
5> PSH
6> JSR -1127403496
7> ENT 2
8> LLA -1
9> PSH
10> IMM 1
11> SI
12> LLA -2
13> PSH
14> IMM 1
15> SI
16> LLA -2
17> LI
18> PSH
19> LLA 2
20> LI
21> LE
22> BZ -1127403096
23> LLA -1
24> PSH
25> LLA -1
26> LI
27> PSH
28> IMM 2
29> MUL
30> SI
31> LLA -2
32> PSH
33> LI
34> PSH
35> IMM 1
36> ADD
37> SI
38> PSH
39> IMM 1
40> SUB
41> JMP -1127403384
42> LLA -2
43> LI
44> PSH
45> LLA 2
46> LI
47> LE
48> BZ -1127403096
49> LLA -1
50> PSH
51> LLA -1
52> LI
53> PSH
54> IMM 2
55> MUL
56> SI
57> LLA -2
58> PSH
59> LI
60> PSH
61> IMM 1
62> ADD
63> SI
64> PSH
65> IMM 1
66> SUB
67> JMP -1127403384
68> LLA -2
69> LI
70> PSH
71> LLA 2
72> LI
73> LE
74> BZ -1127403096
75> LLA -1
76> PSH
77> LLA -1
78> LI
79> PSH
80> IMM 2
81> MUL
82> SI
83> LLA -2
84> PSH
85> LI
86> PSH
87> IMM 1
88> ADD
89> SI
90> PSH
91> IMM 1
92> SUB
93> JMP -1127403384
94> LLA -2
95> LI
96> PSH
97> LLA 2
98> LI
99> LE
100> BZ -1127403096
101> LLA -1
102> LI
103> LEV
104> ADJ 1
105> PSH
106> PRTF
power2(3)=8
107> ADJ 2
108> LEV
109> PSH
110> EXIT
exit(12) cycle = 110

power2(3)=8
exit(12) cycle = 110

## AsmFib Output

1> ENT 0
2> IMM 1159917913
3> PSH
4> IMM 7
5> PSH
6> JSR 2058600464
7> ENT 0
8> LLA 2
9> LI
10> PSH
11> IMM 0
12> LE
13> BZ 2058600576
14> LLA 2
15> LI
16> PSH
17> IMM 1
18> EQ
19> BZ 2058600672
20> LLA 2
21> LI
22> PSH
23> IMM 1
24> SUB
25> PSH
26> JSR 2058600464
27> ENT 0
28> LLA 2
29> LI
30> PSH
31> IMM 0
32> LE
33> BZ 2058600576
34> LLA 2
35> LI
36> PSH
37> IMM 1
38> EQ
39> BZ 2058600672
40> LLA 2
41> LI
42> PSH
43> IMM 1
44> SUB
45> PSH
46> JSR 2058600464
47> ENT 0
48> LLA 2
49> LI
50> PSH
51> IMM 0
52> LE
53> BZ 2058600576
54> LLA 2
55> LI
56> PSH
57> IMM 1
58> EQ
59> BZ 2058600672
60> LLA 2
61> LI
62> PSH
63> IMM 1
64> SUB
65> PSH
66> JSR 2058600464
67> ENT 0
68> LLA 2
69> LI
70> PSH
71> IMM 0
72> LE
73> BZ 2058600576
74> LLA 2
75> LI
76> PSH
77> IMM 1
78> EQ
79> BZ 2058600672
80> LLA 2
81> LI
82> PSH
83> IMM 1
84> SUB
85> PSH
86> JSR 2058600464
87> ENT 0
88> LLA 2
89> LI
90> PSH
91> IMM 0
92> LE
93> BZ 2058600576
94> LLA 2
95> LI
96> PSH
97> IMM 1
98> EQ
99> BZ 2058600672
100> LLA 2
101> LI
102> PSH
103> IMM 1
104> SUB
105> PSH
106> JSR 2058600464
107> ENT 0
108> LLA 2
109> LI
110> PSH
111> IMM 0
112> LE
113> BZ 2058600576
114> LLA 2
115> LI
116> PSH
117> IMM 1
118> EQ
119> BZ 2058600672
120> LLA 2
121> LI
122> PSH
123> IMM 1
124> SUB
125> PSH
126> JSR 2058600464
127> ENT 0
128> LLA 2
129> LI
130> PSH
131> IMM 0
132> LE
133> BZ 2058600576
134> LLA 2
135> LI
136> PSH
137> IMM 1
138> EQ
139> BZ 2058600672
140> IMM 1
141> LEV
142> ADJ 1
143> PSH
144> LLA 2
145> LI
146> PSH
147> IMM 2
148> SUB
149> PSH
150> JSR 2058600464
151> ENT 0
152> LLA 2
153> LI
154> PSH
155> IMM 0
156> LE
157> BZ 2058600576
158> IMM 0
159> LEV
160> ADJ 1
161> ADD
162> LEV
163> ADJ 1
164> PSH
165> LLA 2
166> LI
167> PSH
168> IMM 2
169> SUB
170> PSH
171> JSR 2058600464
172> ENT 0
173> LLA 2
174> LI
175> PSH
176> IMM 0
177> LE
178> BZ 2058600576
179> LLA 2
180> LI
181> PSH
182> IMM 1
183> EQ
184> BZ 2058600672
185> IMM 1
186> LEV
187> ADJ 1
188> ADD
189> LEV
190> ADJ 1
191> PSH
192> LLA 2
193> LI
194> PSH
195> IMM 2
196> SUB
197> PSH
198> JSR 2058600464
199> ENT 0
200> LLA 2
201> LI
202> PSH
203> IMM 0
204> LE
205> BZ 2058600576
206> LLA 2
207> LI
208> PSH
209> IMM 1
210> EQ
211> BZ 2058600672
212> LLA 2
213> LI
214> PSH
215> IMM 1
216> SUB
217> PSH
218> JSR 2058600464
219> ENT 0
220> LLA 2
221> LI
222> PSH
223> IMM 0
224> LE
225> BZ 2058600576
226> LLA 2
227> LI
228> PSH
229> IMM 1
230> EQ
231> BZ 2058600672
232> IMM 1
233> LEV
234> ADJ 1
235> PSH
236> LLA 2
237> LI
238> PSH
239> IMM 2
240> SUB
241> PSH
242> JSR 2058600464
243> ENT 0
244> LLA 2
245> LI
246> PSH
247> IMM 0
248> LE
249> BZ 2058600576
250> IMM 0
251> LEV
252> ADJ 1
253> ADD
254> LEV
255> ADJ 1
256> ADD
257> LEV
258> ADJ 1
259> PSH
260> LLA 2
261> LI
262> PSH
263> IMM 2
264> SUB
265> PSH
266> JSR 2058600464
267> ENT 0
268> LLA 2
269> LI
270> PSH
271> IMM 0
272> LE
273> BZ 2058600576
274> LLA 2
275> LI
276> PSH
277> IMM 1
278> EQ
279> BZ 2058600672
280> LLA 2
281> LI
282> PSH
283> IMM 1
284> SUB
285> PSH
286> JSR 2058600464
287> ENT 0
288> LLA 2
289> LI
290> PSH
291> IMM 0
292> LE
293> BZ 2058600576
294> LLA 2
295> LI
296> PSH
297> IMM 1
298> EQ
299> BZ 2058600672
300> LLA 2
301> LI
302> PSH
303> IMM 1
304> SUB
305> PSH
306> JSR 2058600464
307> ENT 0
308> LLA 2
309> LI  
310> PSH
311> IMM 0
312> LE
313> BZ 2058600576
314> LLA 2
315> LI
316> PSH
317> IMM 1
318> EQ
319> BZ 2058600672
320> IMM 1
321> LEV
322> ADJ 1
323> PSH
324> LLA 2
325> LI
326> PSH
327> IMM 2
328> SUB
329> PSH
330> JSR 2058600464
331> ENT 0
332> LLA 2
333> LI
334> PSH
335> IMM 0
336> LE
337> BZ 2058600576
338> IMM 0
339> LEV
340> ADJ 1
341> ADD
342> LEV
343> ADJ 1
344> PSH
345> LLA 2
346> LI
347> PSH
348> IMM 2
349> SUB
350> PSH
351> JSR 2058600464
352> ENT 0
353> LLA 2
354> LI
355> PSH
356> IMM 0
357> LE
358> BZ 2058600576
359> LLA 2
360> LI
361> PSH
362> IMM 1
363> EQ
364> BZ 2058600672
365> IMM 1
366> LEV
367> ADJ 1
368> ADD
369> LEV
370> ADJ 1
371> ADD
372> LEV
373> ADJ 1
374> PSH
375> LLA 2
376> LI
377> PSH
378> IMM 2
379> SUB
380> PSH
381> JSR 2058600464
382> ENT 0
383> LLA 2
384> LI
385> PSH
386> IMM 0
387> LE
388> BZ 2058600576
389> LLA 2
390> LI
391> PSH
392> IMM 1
393> EQ
394> BZ 2058600672
395> LLA 2
396> LI
397> PSH
398> IMM 1
399> SUB
400> PSH
401> JSR 2058600464
402> ENT 0
403> LLA 2
404> LI
405> PSH
406> IMM 0
407> LE
408> BZ 2058600576
409> LLA 2
410> LI
411> PSH
412> IMM 1
413> EQ
414> BZ 2058600672
415> LLA 2
416> LI
417> PSH
418> IMM 1
419> SUB
420> PSH
421> JSR 2058600464
422> ENT 0
423> LLA 2
424> LI
425> PSH
426> IMM 0
427> LE
428> BZ 2058600576
429> LLA 2
430> LI
431> PSH
432> IMM 1
433> EQ
434> BZ 2058600672
435> LLA 2
436> LI
437> PSH
438> IMM 1
439> SUB
440> PSH
441> JSR 2058600464
442> ENT 0
443> LLA 2
444> LI
445> PSH
446> IMM 0
447> LE
448> BZ 2058600576
449> LLA 2
450> LI
451> PSH
452> IMM 1
453> EQ
454> BZ 2058600672
455> IMM 1
456> LEV
457> ADJ 1
458> PSH
459> LLA 2
460> LI
461> PSH
462> IMM 2
463> SUB
464> PSH
465> JSR 2058600464
466> ENT 0
467> LLA 2
468> LI
469> PSH
470> IMM 0
471> LE
472> BZ 2058600576
473> IMM 0
474> LEV
475> ADJ 1
476> ADD
477> LEV
478> ADJ 1
479> PSH
480> LLA 2
481> LI
482> PSH
483> IMM 2
484> SUB
485> PSH
486> JSR 2058600464
487> ENT 0
488> LLA 2
489> LI
490> PSH
491> IMM 0
492> LE
493> BZ 2058600576
494> LLA 2
495> LI
496> PSH
497> IMM 1
498> EQ
499> BZ 2058600672
500> IMM 1
501> LEV
502> ADJ 1
503> ADD
504> LEV
505> ADJ 1
506> PSH
507> LLA 2
508> LI
509> PSH
510> IMM 2
511> SUB
512> PSH
513> JSR 2058600464
514> ENT 0
515> LLA 2
516> LI
517> PSH
518> IMM 0
519> LE
520> BZ 2058600576
521> LLA 2
522> LI
523> PSH
524> IMM 1
525> EQ
526> BZ 2058600672
527> LLA 2
528> LI
529> PSH
530> IMM 1
531> SUB
532> PSH
533> JSR 2058600464
534> ENT 0
535> LLA 2
536> LI
537> PSH
538> IMM 0
539> LE
540> BZ 2058600576
541> LLA 2
542> LI
543> PSH
544> IMM 1
545> EQ
546> BZ 2058600672
547> IMM 1
548> LEV
549> ADJ 1
550> PSH
551> LLA 2
552> LI
553> PSH
554> IMM 2
555> SUB
556> PSH
557> JSR 2058600464
558> ENT 0
559> LLA 2
560> LI
561> PSH
562> IMM 0
563> LE
564> BZ 2058600576
565> IMM 0
566> LEV
567> ADJ 1
568> ADD
569> LEV
570> ADJ 1
571> ADD
572> LEV
573> ADJ 1
574> ADD
575> LEV
576> ADJ 1
577> PSH
578> LLA 2
579> LI
580> PSH
581> IMM 2
582> SUB
583> PSH
584> JSR 2058600464
585> ENT 0
586> LLA 2
587> LI
588> PSH
589> IMM 0
590> LE
591> BZ 2058600576
592> LLA 2
593> LI
594> PSH
595> IMM 1
596> EQ
597> BZ 2058600672
598> LLA 2
599> LI
600> PSH
601> IMM 1
602> SUB
603> PSH
604> JSR 2058600464
605> ENT 0
606> LLA 2
607> LI
608> PSH
609> IMM 0
610> LE
611> BZ 2058600576
612> LLA 2
613> LI
614> PSH
615> IMM 1
616> EQ
617> BZ 2058600672
618> LLA 2
619> LI
620> PSH
621> IMM 1
622> SUB
623> PSH
624> JSR 2058600464
625> ENT 0
626> LLA 2
627> LI
628> PSH
629> IMM 0
630> LE
631> BZ 2058600576
632> LLA 2
633> LI
634> PSH
635> IMM 1
636> EQ
637> BZ 2058600672
638> LLA 2
639> LI
640> PSH
641> IMM 1
642> SUB
643> PSH
644> JSR 2058600464
645> ENT 0
646> LLA 2
647> LI
648> PSH
649> IMM 0
650> LE
651> BZ 2058600576
652> LLA 2
653> LI
654> PSH
655> IMM 1
656> EQ
657> BZ 2058600672
658> LLA 2
659> LI
660> PSH
661> IMM 1
662> SUB
663> PSH
664> JSR 2058600464
665> ENT 0
666> LLA 2
667> LI
668> PSH
669> IMM 0
670> LE
671> BZ 2058600576
672> LLA 2
673> LI
674> PSH
675> IMM 1
676> EQ
677> BZ 2058600672
678> IMM 1
679> LEV
680> ADJ 1
681> PSH
682> LLA 2
683> LI
684> PSH
685> IMM 2
686> SUB
687> PSH
688> JSR 2058600464
689> ENT 0
690> LLA 2
691> LI
692> PSH
693> IMM 0
694> LE
695> BZ 2058600576
696> IMM 0
697> LEV
698> ADJ 1
699> ADD
700> LEV
701> ADJ 1
702> PSH
703> LLA 2
704> LI
705> PSH
706> IMM 2
707> SUB
708> PSH
709> JSR 2058600464
710> ENT 0
711> LLA 2
712> LI
713> PSH
714> IMM 0
715> LE
716> BZ 2058600576
717> LLA 2
718> LI
719> PSH
720> IMM 1
721> EQ
722> BZ 2058600672
723> IMM 1
724> LEV
725> ADJ 1
726> ADD
727> LEV
728> ADJ 1
729> PSH
730> LLA 2
731> LI
732> PSH
733> IMM 2
734> SUB
735> PSH
736> JSR 2058600464
737> ENT 0
738> LLA 2
739> LI
740> PSH
741> IMM 0
742> LE
743> BZ 2058600576
744> LLA 2
745> LI
746> PSH
747> IMM 1
748> EQ
749> BZ 2058600672
750> LLA 2
751> LI
752> PSH
753> IMM 1
754> SUB
755> PSH
756> JSR 2058600464
757> ENT 0
758> LLA 2
759> LI
760> PSH
761> IMM 0
762> LE
763> BZ 2058600576
764> LLA 2
765> LI
766> PSH
767> IMM 1
768> EQ
769> BZ 2058600672
770> IMM 1
771> LEV
772> ADJ 1
773> PSH
774> LLA 2
775> LI
776> PSH
777> IMM 2
778> SUB
779> PSH
780> JSR 2058600464
781> ENT 0
782> LLA 2
783> LI
784> PSH
785> IMM 0
786> LE
787> BZ 2058600576
788> IMM 0
789> LEV
790> ADJ 1
791> ADD
792> LEV
793> ADJ 1
794> ADD
795> LEV
796> ADJ 1
797> PSH
798> LLA 2
799> LI
800> PSH
801> IMM 2
802> SUB
803> PSH
804> JSR 2058600464
805> ENT 0
806> LLA 2
807> LI
808> PSH
809> IMM 0
810> LE
811> BZ 2058600576
812> LLA 2
813> LI
814> PSH
815> IMM 1
816> EQ
817> BZ 2058600672
818> LLA 2
819> LI
820> PSH
821> IMM 1
822> SUB
823> PSH
824> JSR 2058600464
825> ENT 0
826> LLA 2
827> LI
828> PSH
829> IMM 0
830> LE
831> BZ 2058600576
832> LLA 2
833> LI
834> PSH
835> IMM 1
836> EQ
837> BZ 2058600672
838> LLA 2
839> LI
840> PSH
841> IMM 1
842> SUB
843> PSH
844> JSR 2058600464
845> ENT 0
846> LLA 2
847> LI
848> PSH
849> IMM 0
850> LE
851> BZ 2058600576
852> LLA 2
853> LI
854> PSH
855> IMM 1
856> EQ
857> BZ 2058600672
858> IMM 1
859> LEV
860> ADJ 1
861> PSH
862> LLA 2
863> LI
864> PSH
865> IMM 2
866> SUB
867> PSH
868> JSR 2058600464
869> ENT 0
870> LLA 2
871> LI
872> PSH
873> IMM 0
874> LE
875> BZ 2058600576
876> IMM 0
877> LEV
878> ADJ 1
879> ADD
880> LEV
881> ADJ 1
882> PSH
883> LLA 2
884> LI
885> PSH
886> IMM 2
887> SUB
888> PSH
889> JSR 2058600464
890> ENT 0
891> LLA 2
892> LI
893> PSH
894> IMM 0
895> LE
896> BZ 2058600576
897> LLA 2
898> LI
899> PSH
900> IMM 1
901> EQ
902> BZ 2058600672
903> IMM 1
904> LEV
905> ADJ 1
906> ADD
907> LEV
908> ADJ 1
909> ADD
910> LEV
911> ADJ 1
912> ADD
913> LEV
914> ADJ 1
915> PSH
916> PRTF
f(7)=13
917> ADJ 2
918> LEV
919> PSH
920> EXIT
exit(8) cycle = 920

f(7)=13
exit(8) cycle = 920
```

---

## 習題三

[HW3](https://github.com/VinsOrl/_sp/tree/main/HW3)

參考同學，使用ChatGPT和deep seek調試問題

```
while (tk = *p) {
    ++p;
    if (tk == '\n') { // 換行
      if (src) {
        printf("%d: %.*s", line, p - lp, lp); // 印出該行
        lp = p; // lp = p = 新一行的原始碼開頭
        while (le < e) { // 印出上一行的所有目的碼
          printf("  %d: %8.4s", le+1, &"LLA ,IMM ,JMP ,JSR ,BZ  ,BNZ ,ENT ,ADJ ,LEV ,LI  ,LC  ,SI  ,SC  ,PSH ,"
                           "OR  ,XOR ,AND ,EQ  ,NE  ,LT  ,GT  ,LE  ,GE  ,SHL ,SHR ,ADD ,SUB ,MUL ,DIV ,MOD ,"
                           "OPEN,READ,CLOS,PRTF,MALC,FREE,MSET,MCMP,EXIT,"[*++le * 5]);
          if (*le <= ADJ) printf("%d\n", *++le); else printf("\n"); // LLA ,IMM ,JMP ,JSR ,BZ  ,BNZ ,ENT ,ADJ 有一個參數。
        }
      }
      ++line;
    }
  }
```

---

## 習題四

[HW4](https://github.com/VinsOrl/_sp/tree/main/HW4)

參考同學，使用ChatGPT調試問題
```
# -----------------------------------------------------------------------------
# A 64-bit function that returns the multiple value of its three 64-bit integer
# arguments.  The function has signature:
#
#   int64_t mul3(int64_t x, int64_t y, int64_t z)
#
# Note that the parameters have already been passed in rdi, rsi, and rdx.  We
# just have to return the value in rax.
# -----------------------------------------------------------------------------

        .globl  mul3
        
        .text
mul3:
        mov     %rdi, %rax
        imulq     %rsi, %rax
        imulq   %rdx, %rax
        ret    
```

---

## 習題五

[HW5](https://github.com/VinsOrl/_sp/tree/main/HW5)

參考同學，使用ChatGPT，deep seek調試問題和老師的資料

```
	.file	"power.c"
	.text
	.globl	_power
	.def	_power;	.scl	2;	.type	32;	.endef
_power:
LFB10:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$16, %esp
	movl	$1, -4(%ebp)
	movl	$0, -8(%ebp)
	jmp	L2
L3:
	movl	-4(%ebp), %eax
	imull	8(%ebp), %eax
	movl	%eax, -4(%ebp)
	addl	$1, -8(%ebp)
L2:
	movl	-8(%ebp), %eax
	cmpl	12(%ebp), %eax
	jl	L3
	movl	-4(%ebp), %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE10:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "result = %d\12\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB11:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$3, 4(%esp)
	movl	$2, (%esp)
	call	_power
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE11:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
```

---

## 期中考

[Full Source](https://github.com/VinsOrl/_sp/tree/main/MIDTERM%20EXAM)

參考同學，使用ChatGPT，deep seek調試問題和老師的資料

```
	import threading
	import requests
	from bs4 import BeautifulSoup
	from urllib.parse import urljoin
	from utils import is_valid_url, normalize_url
	
	visited = set()
	lock = threading.Lock()
	
	MAX_DEPTH = 2
	DOMAIN = "books.toscrape.com"
	
	def crawl(url, depth):
	    if depth == 0:
	        return
	    try:
	        print(f"Crawling: {url} at depth {depth}")
	
	        response = requests.get(url, timeout=5)
	        if response.status_code != 200:
	            print(f"Failed to retrieve {url}: Status {response.status_code}")
	            return
	
	        soup = BeautifulSoup(response.text, "html.parser")
	        for link in soup.find_all('a'):
	            href = link.get('href')
	            if href:
	                full_url = normalize_url(urljoin(url, href))
	                if is_valid_url(full_url, DOMAIN):
	                    with lock:
	                        if full_url not in visited:
	                            visited.add(full_url)
	                            print(f"Found URL: {full_url}")
	                            with open("output.txt", "a", encoding="utf-8") as f:
	                                f.write(full_url + "\n")
	                    threading.Thread(target=crawl, args=(full_url, depth - 1)).start()
	
	    except Exception as e:
	        print(f"[Error] Failed to crawl {url}: {e}")
	
	if __name__ == "__main__":
	    start_url = f"http://{DOMAIN}"
	    crawl(start_url, MAX_DEPTH)
```

---

## 總結

在這學期的系統程式設計課程中，我不僅學習了編譯器的核心理論，像是詞法分析、語法分析、中間碼生成與目標碼生成等流程，也實際動手實作了這些階段，讓抽象的概念具體而深刻。此外，我深入探究了 C4 虛擬機 的運作機制，並透過一系列富挑戰性的練習題，實現了各種程式語言特性，包括 迴圈、條件判斷、函數呼叫 等控制結構。

這些寶貴的理論知識與實作經驗不僅讓我更理解程式語言背後的底層邏輯，也大幅提升了我在程式設計與解決問題上的能力。我相信，這些技能與訓練將成為我未來在軟體開發領域中強而有力的基礎。

最後，誠摯感謝老師的細心教導與同學們的無私協助，讓我能夠順利且充實地完成這門課程的所有挑戰，也讓我對系統層級的開發有了更深的認識與熱情。

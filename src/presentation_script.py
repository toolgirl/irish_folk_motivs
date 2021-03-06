#!/usr/bin/env python
from tune_fragment import TuneFragment


full_tune = 'gAegGf2gGgAcffAeFB3g22Gd4Ae73B2fBB2cg2cgA2AG2AG22AGBBddgBe2fAgd2gG2BfG2eDdEBddBBc2BFfdfe2dcBdABGGFdcABGGEAA1GBedd3BecfefdgBecfcdegd3e2fEmGABBd2cGd3bBebdaadgedagbeagf2gaabgeeeefeg2ag22eAdGcBdggbfga2gafbgge2AeGEcDEDAABBAcgGABaBgdfegdfc23cBBABGc2GDEGDDEgGegdeGg2fgegadgBadg22effgbegddBFA4FGdGfFga2FgDfaefdggafegd2ed24Bd4dFAGa2gGfBA2eBGAEFEGFGEF4AdGcdcdBdg2bfgdBgAefGe2dgfed2ABGz2GA2BcAG'


tune_chunk = '4Bd4dFAGa2gGfBA2eBGAEFEGFGEF4AdGcdcdBdg2bfgdBgAefGe2dgfed2ABGz2GA2BcAG'
tunefr = TuneFragment({'mode': 'G', 'meter': '6/8', 'abc': full_tune})
tunefr.play()


# timidity -Ow -o - input.mid | lame - output.mp3

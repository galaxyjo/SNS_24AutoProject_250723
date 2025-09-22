
n, dm["rank"], dms, at, elsize
                    note = "\n".join(note)
                % (name, ",".join(inames))
                % (name, ",".join(inames), ",".join(hnames))
                )
                '\t{{"{}",{},{{{{{}}}}},{}, {}}},'.format(
                '\t\tConstructing COMMON block support for "%s"...\n\t\t  %s\n'
                '\t\tConstructing COMMON block support for "%s"...\n\t\t  %s\n\t\t  Hidden: %s\n'
                dadd("--- %s" % (note))
                dms = "-1"
                hnames.append(n)
                idims.append("")
                idims.append("(%s)" % (dm["dims"]))
                if isinstance(note, list):
                inames.append(n)
                name, ",".join(map(lambda v, d: v + d, inames, idims))
                names.append(t[0])
                note = vars[n]["note"]
                tret.append(t)
            "\t%s(f2pyinit%s,F2PYINIT%s)(f2py_setup_%s);"
            '"\t/{}/ {}\\n"'.format(
            "\ttmp = PyFortranObject_New(f2py_{}_def,f2py_init_{});".format(name, name)
            "extern void %s(f2pyinit%s,F2PYINIT%s)(void(*)(%s));"
            % (F_FUNC, lower_name, name.upper(), ",".join(["char*"] * len(inames1)))
            % (F_FUNC, lower_name, name.upper(), name)
            )
            at = capi_maps.c2capi_map[ct]
            cadd(
            cadd("\tf2py_{}_def[i_f2py++].data = {};".format(name, n))
            ct = capi_maps.getctype(vars[n])
            dadd("\\item[]{{}\\verb@%s@{}}" % (capi_maps.getarrdocsign(n, vars[n])))
            dm = capi_maps.getarrdims(n, vars[n])
            dms = dm["dims"].strip()
            else:
            elsize = capi_maps.get_elsize(vars[n])
            F_FUNC = "F_FUNC"
            F_FUNC = "F_FUNC_US"
            fadd("common %s" % (",".join(vnames)))
            fadd("common /{}/ {}".format(name, ",".join(vnames)))
            fadd(f"use {usename}")
            fadd(func2subr.var2fixfortran(vars, n))
            if dm["dims"]:
            if hasnote(vars[n]):
            if isintent_hide(vars[n]):
            if not dms:
            if t[0] not in names:
            outmess(
            ret = ret + findcommonblocks(b, 0)
            ret.append((key, value, vars_))
            vars_ = {v: block["vars"][v] for v in value}
        )
        cadd(
        cadd("}")
        cadd("}\n")
        cadd("\t{NULL}\n};")
        cadd("\tint i_f2py=0;")
        cadd("static FortranDataDef f2py_%s_def[] = {" % (name))
        cadd("static void f2py_init_%s(void) {" % name)
        cadd("static void f2py_setup_{}({}) {{".format(name, inames1_tps))
        dadd("\\begin{description}")
        dadd("\\end{description}")
        dadd("\\subsection{Common block \\texttt{%s}}\n" % (tname))
        else:
        fadd("call setupfunc(%s)" % (",".join(inames)))
        fadd("end\n")
        fadd("external setupfunc")
        fadd("subroutine f2pyinit%s(setupfunc)" % name)
        for b in block["body"]:
        for key, value in block["common"].items():
        for n in inames:
        for n in inames1:
        for n in vnames:
        for t in ret:
        for usename in getuseblocks(m):
        hnames, inames = [], []
        iadd(
        iadd("\tif (tmp == NULL) return NULL;")
        iadd("\tPy_DECREF(tmp);")
        iadd('\tif (F2PyDict_SetItemString(d, "%s", tmp) == -1) return NULL;' % name)
        idims = []
        if "_" in lower_name:
        if hnames:
        if name == "_BLNK_":
        inames1 = rmbadname(inames)
        inames1_tps = ",".join(["char *" + s for s in inames1])
        lower_name = name.lower()
        names = []
        ret["docs"] = ""
        ret["docs"].append(
        return tret
        s[0] = "{}\n      {}".format(s[0], line)
        s[0] = "{}\n{}".format(s[0], line)
        tname = name.replace("_", "\\_")
        tret = []
    chooks = [""]
    def cadd(line, s=chooks):
    def dadd(line, s=doc):
    def fadd(line, s=fwrap):
    def iadd(line, s=ihooks):
    doc = [""]
    elif hasbody(block):
    for name, vnames, vars in findcommonblocks(m):
    fwrap = [""]
    if hascommon(block):
    if len(ret["docs"]) <= 1:
    if top:
    ihooks = [""]
    ret = []
    ret = {"commonhooks": [], "initcommonhooks": [], "docs": ['"COMMON blocks:\\n"']}
    ret["commonhooks"] = chooks
    ret["initcommonhooks"] = ihooks
    ret["latexdoc"] = doc[0]
    return ret
    return ret, fwrap[0]
"""
Build common block mechanism for f2py2e.
Copyright 1999 -- 2011 Pearu Peterson all rights reserved.
Copyright 2011 -- present NumPy Developers.
def buildhooks(m):
def findcommonblocks(block, top=1):
f2py_version = __version__.version
from . import __version__
from . import capi_maps
from . import func2subr
from .auxfuncs import hasbody, hascommon, hasnote, isintent_hide, outmess, getuseblocks
from .crackfortran import rmbadname
NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
Permission to use, modify, and distribute this software is given under the
terms of the NumPy License

pass


                    return newlines
                    return spaces
                    return tabs
                    ttype, value, regex, Whitespace, replacefunc
                    value = value.replace(" ", spaces)
                    value = value.replace("\n", newlines)
                    value = value.replace("\t", tabs)
                    yield current_type, current_value
                (parts[i], left) = self.gobble(parts[i], n)
                )
                current_type = ttype
                current_value += value
                current_value = value
                elif wschar == "\n":
                elif wschar == "\t":
                if current_type is not None:
                if newlines:
                if spaces:
                if tabs:
                if wschar == " ":
                raise self.exception(value)
                raise TypeError
                return wschar
                setattr(self, name, (opt and default or ""))
                setattr(self, name, opt)
                yield from _replace_special(
                yield from _replace_special(ttype, value, regex, Comment.Special)
                yield self.tokentype, value
                yield ttype, self.convert(value)
                yield ttype, self.symbols[value]
                yield ttype, value
            # issubclass() will raise TypeError if first argument is not a class
            # Remove ``left`` tokens from first line, ``n`` from all others.
            # simpler processing
            (parts[0], left) = self.gobble(parts[0], left)
            def replacefunc(wschar):
            else:
            for i in range(1, len(parts)):
            for ttype, value in stream:
            if isinstance(opt, str) and len(opt) == 1:
            if not issubclass(self.exception, Exception):
            if ttype in Keyword:
            if ttype in Name and value in self.names:
            if ttype in String.Doc or ttype in Comment and ttype not in Comment.Preproc:
            if ttype is current_type:
            if ttype is Error:
            if value != "":
            if value in self.symbols:
            names=['foo', 'bar', 'baz'],
            newlines = self.newlines or "\n"
            opt = options.get(name, False)
            options, "case", ["lower", "upper", "capitalize"], "lower"
            options, "codetags", ["XXX", "TODO", "FIXME", "BUG", "NOTE"]
            parts = value.split("\n")
            r"\b(%s)\b" % "|".join([re.escape(tag) for tag in tags if tag])
            raise OptionError("excclass option is not an exception class")
            regex = re.compile(r"\s")
            return "", left - len(value)
            return cls
            return value[left:], 0
            self.newlines += "\n"
            self.tabs += " " * (tabsize - 1)
            self.tokentype = Name.Function
            self.tokentype = string_to_tokentype(tokentype)
            spaces = self.spaces or " "
            spaces, tabs, newlines = self.spaces, self.tabs, self.newlines
            tabs = self.tabs or "\t"
            tokentype=Name.Function,
            value = "\n".join(parts)
            yield current_type, current_value
            yield ttype, value
            yield ttype, value[last:start]
        "\\<^bold>": "\U00002759",
        "\\<^bsub>": "\U000021d8",
        "\\<^bsup>": "\U000021d7",
        "\\<^esub>": "\U000021d9",
        "\\<^esup>": "\U000021d6",
        "\\<^sub>": "\U000021e9",
        "\\<^sup>": "\U000021e7",
        "\\<A>": "\U0001d49c",
        "\\<a>": "\U0001d5ba",
        "\\<AA>": "\U0001d504",
        "\\<aa>": "\U0001d51e",
        "\\<acute>": "\U000000b4",
        "\\<aleph>": "\U00002135",
        "\\<alpha>": "\U000003b1",
        "\\<amalg>": "\U00002a3f",
        "\\<and>": "\U00002227",
        "\\<And>": "\U000022c0",
        "\\<angle>": "\U00002220",
        "\\<approx>": "\U00002248",
        "\\<asymp>": "\U0000224d",
        "\\<B>": "\U0000212c",
        "\\<b>": "\U0001d5bb",
        "\\<bar>": "\U000000a6",
        "\\<BB>": "\U0001d505",
        "\\<bb>": "\U0001d51f",
        "\\<beta>": "\U000003b2",
        "\\<bool>": "\U0001d539",
        "\\<bottom>": "\U000022a5",
        "\\<bowtie>": "\U00002a1d",
        "\\<box>": "\U000025a1",
        "\\<bullet>": "\U00002219",
        "\\<C>": "\U0001d49e",
        "\\<c>": "\U0001d5bc",
        "\\<CC>": "\U0000212d",
        "\\<cc>": "\U0001d520",
        "\\<cdot>": "\U000022c5",
        "\\<cdots>": "\U000022ef",
        "\\<cedilla>": "\U000000b8",
        "\\<cent>": "\U000000a2",
        "\\<chi>": "\U000003c7",
        "\\<circ>": "\U00002218",
        "\\<close>": "\U0000203a",
        "\\<clubsuit>": "\U00002663",
        "\\<Colon>": "\U00002237",
        "\\<complex>": "\U00002102",
        "\\<cong>": "\U00002245",
        "\\<Coprod>": "\U00002210",
        "\\<copyright>": "\U000000a9",
        "\\<currency>": "\U000000a4",
        "\\<D>": "\U0001d49f",
        "\\<d>": "\U0001d5bd",
        "\\<dagger>": "\U00002020",
        "\\<DD>": "\U0001d507",
        "\\<dd>": "\U0001d521",
        "\\<ddagger>": "\U00002021",
        "\\<degree>": "\U000000b0",
        "\\<Delta>": "\U00000394",
        "\\<delta>": "\U000003b4",
        "\\<diamond>": "\U000025c7",
        "\\<diamondsuit>": "\U00002662",
        "\\<dieresis>": "\U000000a8",
        "\\<div>": "\U000000f7",
        "\\<doteq>": "\U00002250",
        "\\<dots>": "\U00002026",
        "\\<down>": "\U00002193",
        "\\<Down>": "\U000021d3",
        "\\<downharpoonleft>": "\U000021c3",
        "\\<downharpoonright>": "\U000021c2",
        "\\<E>": "\U00002130",
        "\\<e>": "\U0001d5be",
        "\\<EE>": "\U0001d508",
        "\\<ee>": "\U0001d522",
        "\\<eight>": "\U0001d7f4",
        "\\<emptyset>": "\U00002205",
        "\\<epsilon>": "\U000003b5",
        "\\<equiv>": "\U00002261",
        "\\<eta>": "\U000003b7",
        "\\<euro>": "\U000020ac",
        "\\<exclamdown>": "\U000000a1",
        "\\<exists>": "\U00002203",
        "\\<F>": "\U00002131",
        "\\<f>": "\U0001d5bf",
        "\\<FF>": "\U0001d509",
        "\\<ff>": "\U0001d523",
        "\\<five>": "\U0001d7f1",
        "\\<flat>": "\U0000266d",
        "\\<forall>": "\U00002200",
        "\\<four>": "\U0001d7f0",
        "\\<frown>": "\U00002322",
        "\\<G>": "\U0001d4a2",
        "\\<g>": "\U0001d5c0",
        "\\<Gamma>": "\U00000393",
        "\\<gamma>": "\U000003b3",
        "\\<ge>": "\U00002265",
        "\\<GG>": "\U0001d50a",
        "\\<gg>": "\U0001d524",
        "\\<ggreater>": "\U0000226b",
        "\\<greaterapprox>": "\U00002a86",
        "\\<greatersim>": "\U00002273",
        "\\<guillemotleft>": "\U000000ab",
        "\\<guillemotright>": "\U000000bb",
        "\\<H>": "\U0000210b",
        "\\<h>": "\U0001d5c1",
        "\\<heartsuit>": "\U00002661",
        "\\<here>": "\U00002302",
        "\\<HH>": "\U0000210c",
        "\\<hh>": "\U0001d525",
        "\\<hookleftarrow>": "\U000021a9",
        "\\<hookrightarrow>": "\U000021aa",
        "\\<hungarumlaut>": "\U000002dd",
        "\\<hyphen>": "\U000000ad",
        "\\<I>": "\U00002110",
        "\\<i>": "\U0001d5c2",
        "\\<II>": "\U00002111",
        "\\<ii>": "\U0001d526",
        "\\<in>": "\U00002208",
        "\\<index>": "\U00000131",
        "\\<infinity>": "\U0000221e",
        "\\<int>": "\U00002124",
        "\\<integral>": "\U0000222b",
        "\\<inter>": "\U00002229",
        "\\<Inter>": "\U000022c2",
        "\\<inverse>": "\U000000af",
        "\\<iota>": "\U000003b9",
        "\\<J>": "\U0001d4a5",
        "\\<j>": "\U0001d5c3",
        "\\<JJ>": "\U0001d50d",
        "\\<jj>": "\U0001d527",
        "\\<Join>": "\U000022c8",
        "\\<K>": "\U0001d4a6",
        "\\<k>": "\U0001d5c4",
        "\\<kappa>": "\U000003ba",
        "\\<KK>": "\U0001d50e",
        "\\<kk>": "\U0001d528",
        "\\<L>": "\U00002112",
        "\\<l>": "\U0001d5c5",
        "\\<Lambda>": "\U0000039b",
        "\\<lambda>": "\U000003bb",
        "\\<langle>": "\U000027e8",
        "\\<lbrace>": "\U00002983",
        "\\<lbrakk>": "\U000027e6",
        "\\<lceil>": "\U00002308",
        "\\<le>": "\U00002264",
        "\\<leadsto>": "\U0000219d",
        "\\<leftarrow>": "\U00002190",
        "\\<Leftarrow>": "\U000021d0",
        "\\<leftharpoondown>": "\U000021bd",
        "\\<leftharpoonup>": "\U000021bc",
        "\\<leftrightarrow>": "\U00002194",
        "\\<Leftrightarrow>": "\U000021d4",
        "\\<lessapprox>": "\U00002a85",
        "\\<lesssim>": "\U00002272",
        "\\<lfloor>": "\U0000230a",
        "\\<lhd>": "\U000022b2",
        "\\<LL>": "\U0001d50f",
        "\\<ll>": "\U0001d529",
        "\\<lless>": "\U0000226a",
        "\\<longleftarrow>": "\U000027f5",
        "\\<Longleftarrow>": "\U000027f8",
        "\\<longleftrightarrow>": "\U000027f7",
        "\\<Longleftrightarrow>": "\U000027fa",
        "\\<longmapsto>": "\U000027fc",
        "\\<longrightarrow>": "\U000027f6",
        "\\<Longrightarrow>": "\U000027f9",
        "\\<lozenge>": "\U000025ca",
        "\\<lparr>": "\U00002987",
        "\\<M>": "\U00002133",
        "\\<m>": "\U0001d5c6",
        "\\<mapsto>": "\U000021a6",
        "\\<mho>": "\U00002127",
        "\\<midarrow>": "\U00002500",
        "\\<Midarrow>": "\U00002550",
        "\\<minusplus>": "\U00002213",
        "\\<MM>": "\U0001d510",
        "\\<mm>": "\U0001d52a",
        "\\<mu>": "\U000003bc",
        "\\<N>": "\U0001d4a9",
        "\\<n>": "\U0001d5c7",
        "\\<nabla>": "\U00002207",
        "\\<nat>": "\U00002115",
        "\\<natural>": "\U0000266e",
        "\\<newline>": "\U000023ce",
        "\\<nexists>": "\U00002204",
        "\\<nine>": "\U0001d7f5",
        "\\<NN>": "\U0001d511",
        "\\<nn>": "\U0001d52b",
        "\\<not>": "\U000000ac",
        "\\<noteq>": "\U00002260",
        "\\<notin>": "\U00002209",
        "\\<nu>": "\U000003bd",
        "\\<O>": "\U0001d4aa",
        "\\<o>": "\U0001d5c8",
        "\\<odot>": "\U00002299",
        "\\<Odot>": "\U00002a00",
        "\\<ointegral>": "\U0000222e",
        "\\<Omega>": "\U000003a9",
        "\\<omega>": "\U000003c9",
        "\\<ominus>": "\U00002296",
        "\\<one>": "\U0001d7ed",
        "\\<onehalf>": "\U000000bd",
        "\\<onequarter>": "\U000000bc",
        "\\<OO>": "\U0001d512",
        "\\<oo>": "\U0001d52c",
        "\\<open>": "\U00002039",
        "\\<oplus>": "\U00002295",
        "\\<Oplus>": "\U00002a01",
        "\\<or>": "\U00002228",
        "\\<Or>": "\U000022c1",
        "\\<ordfeminine>": "\U000000aa",
        "\\<ordmasculine>": "\U000000ba",
        "\\<oslash>": "\U00002298",
        "\\<otimes>": "\U00002297",
        "\\<Otimes>": "\U00002a02",
        "\\<P>": "\U0001d4ab",
        "\\<p>": "\U0001d5c9",
        "\\<paragraph>": "\U000000b6",
        "\\<parallel>": "\U00002225",
        "\\<partial>": "\U00002202",
        "\\<Phi>": "\U000003a6",
        "\\<phi>": "\U000003c6",
        "\\<Pi>": "\U000003a0",
        "\\<pi>": "\U000003c0",
        "\\<plusminus>": "\U000000b1",
        "\\<pounds>": "\U000000a3",
        "\\<PP>": "\U0001d513",
        "\\<pp>": "\U0001d52d",
        "\\<prec>": "\U0000227a",
        "\\<preceq>": "\U0000227c",
        "\\<Prod>": "\U0000220f",
        "\\<propto>": "\U0000221d",
        "\\<Psi>": "\U000003a8",
        "\\<psi>": "\U000003c8",
        "\\<Q>": "\U0001d4ac",
        "\\<q>": "\U0001d5ca",
        "\\<QQ>": "\U0001d514",
        "\\<qq>": "\U0001d52e",
        "\\<questiondown>": "\U000000bf",
        "\\<R>": "\U0000211b",
        "\\<r>": "\U0001d5cb",
        "\\<rangle>": "\U000027e9",
        "\\<rat>": "\U0000211a",
        "\\<rbrace>": "\U00002984",
        "\\<rbrakk>": "\U000027e7",
        "\\<rceil>": "\U00002309",
        "\\<real>": "\U0000211d",
        "\\<registered>": "\U000000ae",
        "\\<restriction>": "\U000021be",
        "\\<rfloor>": "\U0000230b",
        "\\<rhd>": "\U000022b3",
        "\\<rho>": "\U000003c1",
        "\\<rightarrow>": "\U00002192",
        "\\<Rightarrow>": "\U000021d2",
        "\\<rightharpoondown>": "\U000021c1",
        "\\<rightharpoonup>": "\U000021c0",
        "\\<rightleftharpoons>": "\U000021cc",
        "\\<rparr>": "\U00002988",
        "\\<RR>": "\U0000211c",
        "\\<rr>": "\U0001d52f",
        "\\<S>": "\U0001d4ae",
        "\\<s>": "\U0001d5cc",
        "\\<section>": "\U000000a7",
        "\\<setminus>": "\U00002216",
        "\\<seven>": "\U0001d7f3",
        "\\<sharp>": "\U0000266f",
        "\\<Sigma>": "\U000003a3",
        "\\<sigma>": "\U000003c3",
        "\\<sim>": "\U0000223c",
        "\\<simeq>": "\U00002243",
        "\\<six>": "\U0001d7f2",
        "\\<smile>": "\U00002323",
        "\\<some>": "\U000003f5",
        "\\<spadesuit>": "\U00002660",
        "\\<sqinter>": "\U00002293",
        "\\<Sqinter>": "\U00002a05",
        "\\<sqsubset>": "\U0000228f",
        "\\<sqsubseteq>": "\U00002291",
        "\\<sqsupset>": "\U00002290",
        "\\<sqsupseteq>": "\U00002292",
        "\\<squnion>": "\U00002294",
        "\\<Squnion>": "\U00002a06",
        "\\<SS>": "\U0001d516",
        "\\<ss>": "\U0001d530",
        "\\<star>": "\U000022c6",
        "\\<stileturn>": "\U000022a3",
        "\\<struct>": "\U000022c4",
        "\\<subset>": "\U00002282",
        "\\<subseteq>": "\U00002286",
        "\\<succ>": "\U0000227b",
        "\\<succeq>": "\U0000227d",
        "\\<Sum>": "\U00002211",
        "\\<supset>": "\U00002283",
        "\\<supseteq>": "\U00002287",
        "\\<surd>": "\U0000221a",
        "\\<T>": "\U0001d4af",
        "\\<t>": "\U0001d5cd",
        "\\<tau>": "\U000003c4",
        "\\<Theta>": "\U00000398",
        "\\<theta>": "\U000003b8",
        "\\<three>": "\U0001d7ef",
        "\\<threequarters>": "\U000000be",
        "\\<times>": "\U000000d7",
        "\\<top>": "\U000022a4",
        "\\<triangle>": "\U000025b3",
        "\\<triangleleft>": "\U000025c3",
        "\\<triangleq>": "\U0000225c",
        "\\<triangleright>": "\U000025b9",
        "\\<TT>": "\U0001d517",
        "\\<tt>": "\U0001d531",
        "\\<tturnstile>": "\U000022a9",
        "\\<TTurnstile>": "\U000022ab",
        "\\<turnstile>": "\U000022a2",
        "\\<Turnstile>": "\U000022a8",
        "\\<two>": "\U0001d7ee",
        "\\<U>": "\U0001d4b0",
        "\\<u>": "\U0001d5ce",
        "\\<union>": "\U0000222a",
        "\\<Union>": "\U000022c3",
        "\\<unlhd>": "\U000022b4",
        "\\<unrhd>": "\U000022b5",
        "\\<up>": "\U00002191",
        "\\<Up>": "\U000021d1",
        "\\<updown>": "\U00002195",
        "\\<Updown>": "\U000021d5",
        "\\<upharpoonleft>": "\U000021bf",
        "\\<upharpoonright>": "\U000021be",
        "\\<uplus>": "\U0000228e",
        "\\<Uplus>": "\U00002a04",
        "\\<Upsilon>": "\U000003a5",
        "\\<upsilon>": "\U000003c5",
        "\\<UU>": "\U0001d518",
        "\\<uu>": "\U0001d532",
        "\\<V>": "\U0001d4b1",
        "\\<v>": "\U0001d5cf",
        "\\<VV>": "\U0001d519",
        "\\<vv>": "\U0001d533",
        "\\<W>": "\U0001d4b2",
        "\\<w>": "\U0001d5d0",
        "\\<wp>": "\U00002118",
        "\\<wrong>": "\U00002240",
        "\\<WW>": "\U0001d51a",
        "\\<ww>": "\U0001d534",
        "\\<X>": "\U0001d4b3",
        "\\<x>": "\U0001d5d1",
        "\\<Xi>": "\U0000039e",
        "\\<xi>": "\U000003be",
        "\\<XX>": "\U0001d51b",
        "\\<xx>": "\U0001d535",
        "\\<Y>": "\U0001d4b4",
        "\\<y>": "\U0001d5d2",
        "\\<yen>": "\U000000a5",
        "\\<YY>": "\U0001d51c",
        "\\<yy>": "\U0001d536",
        "\\<Z>": "\U0001d4b5",
        "\\<z>": "\U0001d5d3",
        "\\<zero>": "\U0001d7ec",
        "\\<zeta>": "\U000003b6",
        "\\<ZZ>": "\U00002128",
        "\\<zz>": "\U0001d537",
        "\\aleph": "\U00002135",
        "\\alpha": "\U000003b1",
        "\\angle": "\U00002220",
        "\\approx": "\U00002248",
        "\\asymp": "\U0000224d",
        "\\beta": "\U000003b2",
        "\\bigcap": "\U000022c2",
        "\\bigcup": "\U000022c3",
        "\\bigodot": "\U00002a00",
        "\\bigoplus": "\U00002a01",
        "\\bigotimes": "\U00002a02",
        "\\bigplus": "\U00002a04",
        "\\Bigsqcap": "\U00002a05",
        "\\bigsqcup": "\U00002a06",
        "\\bigvee": "\U000022c1",
        "\\bigwedge": "\U000022c0",
        "\\bot": "\U000022a5",
        "\\bowtie": "\U00002a1d",
        "\\Box": "\U000025a1",
        "\\cap": "\U00002229",
        "\\cdot": "\U000022c5",
        "\\cdots": "\U000022ef",
        "\\chi": "\U000003c7",
        "\\circ": "\U00002218",
        "\\clubsuit": "\U00002663",
        "\\cong": "\U00002245",
        "\\coprod": "\U00002210",
        "\\copyright": "\U000000a9",
        "\\cup": "\U0000222a",
        "\\dagger": "\U00002020",
        "\\dashv": "\U000022a3",
        "\\ddagger": "\U00002021",
        "\\Delta": "\U00000394",
        "\\delta": "\U000003b4",
        "\\Diamond": "\U000025c7",
        "\\diamondsuit": "\U00002662",
        "\\div": "\U000000f7",
        "\\doteq": "\U00002250",
        "\\dots": "\U00002026",
        "\\downarrow": "\U00002193",
        "\\Downarrow": "\U000021d3",
        "\\downharpoonleft": "\U000021c3",
        "\\downharpoonright": "\U000021c2",
        "\\emptyset": "\U00002205",
        "\\equiv": "\U00002261",
        "\\eta": "\U000003b7",
        "\\euro": "\U000020ac",
        "\\exists": "\U00002203",
        "\\flat": "\U0000266d",
        "\\flqq": "\U000000ab",
        "\\forall": "\U00002200",
        "\\frqq": "\U000000bb",
        "\\Gamma": "\U00000393",
        "\\gamma": "\U000003b3",
        "\\ge": "\U00002265",
        "\\gg": "\U0000226b",
        "\\gtrapprox": "\U00002a86",
        "\\gtrsim": "\U00002273",
        "\\heartsuit": "\U00002661",
        "\\hookleftarrow": "\U000021a9",
        "\\hookrightarrow": "\U000021aa",
        "\\in": "\U00002208",
        "\\infty": "\U0000221e",
        "\\int": "\U0000222b",
        "\\iota": "\U000003b9",
        "\\Join": "\U000022c8",
        "\\kappa": "\U000003ba",
        "\\Lambda": "\U0000039b",
        "\\lambda": "\U000003bb",
        "\\langle": "\U000027e8",
        "\\lceil": "\U00002308",
        "\\le": "\U00002264",
        "\\leadsto": "\U0000219d",
        "\\leftarrow": "\U00002190",
        "\\Leftarrow": "\U000021d0",
        "\\leftharpoondown": "\U000021bd",
        "\\leftharpoonup": "\U000021bc",
        "\\leftrightarrow": "\U00002194",
        "\\Leftrightarrow": "\U000021d4",
        "\\lessapprox": "\U00002a85",
        "\\lesssim": "\U00002272",
        "\\lfloor": "\U0000230a",
        "\\lhd": "\U000022b2",
        "\\ll": "\U0000226a",
        "\\longleftarrow": "\U000027f5",
        "\\Longleftarrow": "\U000027f8",
        "\\longleftrightarrow": "\U000027f7",
        "\\Longleftrightarrow": "\U000027fa",
        "\\longmapsto": "\U000027fc",
        "\\longrightarrow": "\U000027f6",
        "\\Longrightarrow": "\U000027f9",
        "\\mapsto": "\U000021a6",
        "\\mid": "\U000000a6",
        "\\models": "\U000022a8",
        "\\mp": "\U00002213",
        "\\mu": "\U000003bc",
        "\\nabla": "\U00002207",
        "\\natural": "\U0000266e",
        "\\neg": "\U000000ac",
        "\\nexists": "\U00002204",
        "\\notin": "\U00002209",
        "\\nu": "\U000003bd",
        "\\odot": "\U00002299",
        "\\oint": "\U0000222e",
        "\\Omega": "\U000003a9",
        "\\omega": "\U000003c9",
        "\\ominus": "\U00002296",
        "\\oplus": "\U00002295",
        "\\oslash": "\U00002298",
        "\\otimes": "\U00002297",
        "\\parallel": "\U00002225",
        "\\partial": "\U00002202",
        "\\Phi": "\U000003a6",
        "\\Pi": "\U000003a0",
        "\\pi": "\U000003c0",
        "\\pm": "\U000000b1",
        "\\pounds": "\U000000a3",
        "\\prec": "\U0000227a",
        "\\preceq": "\U0000227c",
        "\\prod": "\U0000220f",
        "\\propto": "\U0000221d",
        "\\Psi": "\U000003a8",
        "\\psi": "\U000003c8",
        "\\rangle": "\U000027e9",
        "\\rceil": "\U00002309",
        "\\relbar": "\U00002500",
        "\\Relbar": "\U00002550",
        "\\restriction": "\U000021be",
        "\\rfloor": "\U0000230b",
        "\\rhd": "\U000022b3",
        "\\rightarrow": "\U00002192",
        "\\Rightarrow": "\U000021d2",
        "\\rightharpoondown": "\U000021c1",
        "\\rightharpoonup": "\U000021c0",
        "\\rightleftharpoons": "\U000021cc",
        "\\setminus": "\U00002216",
        "\\sharp": "\U0000266f",
        "\\Sigma": "\U000003a3",
        "\\sigma": "\U000003c3",
        "\\sim": "\U0000223c",
        "\\simeq": "\U00002243",
        "\\spadesuit": "\U00002660",
        "\\sqcap": "\U00002293",
        "\\sqcup": "\U00002294",
        "\\sqsubset": "\U0000228f",
        "\\sqsubseteq": "\U00002291",
        "\\sqsupset": "\U00002290",
        "\\sqsupseteq": "\U00002292",
        "\\star": "\U000022c6",
        "\\subset": "\U00002282",
        "\\subseteq": "\U00002286",
        "\\succ": "\U0000227b",
        "\\succeq": "\U0000227d",
        "\\sum": "\U00002211",
        "\\supset": "\U00002283",
        "\\supseteq": "\U00002287",
        "\\surd": "\U0000221a",
        "\\tau": "\U000003c4",
        "\\textcent": "\U000000a2",
        "\\textcurrency": "\U000000a4",
        "\\textdegree": "\U000000b0",
        "\\textonehalf": "\U000000bd",
        "\\textonequarter": "\U000000bc",
        "\\textordfeminine": "\U000000aa",
        "\\textordmasculine": "\U000000ba",
        "\\textregistered": "\U000000ae",
        "\\textthreequarters": "\U000000be",
        "\\Theta": "\U00000398",
        "\\times": "\U000000d7",
        "\\top": "\U000022a4",
        "\\triangle": "\U000025b3",
        "\\triangleleft": "\U000025c3",
        "\\triangleq": "\U0000225c",
        "\\triangleright": "\U000025b9",
        "\\unlhd": "\U000022b4",
        "\\unrhd": "\U000022b5",
        "\\uparrow": "\U00002191",
        "\\Uparrow": "\U000021d1",
        "\\updownarrow": "\U00002195",
        "\\Updownarrow": "\U000021d5",
        "\\upharpoonleft": "\U000021bf",
        "\\upharpoonright": "\U000021be",
        "\\uplus": "\U0000228e",
        "\\Upsilon": "\U000003a5",
        "\\upsilon": "\U000003c5",
        "\\varepsilon": "\U000003b5",
        "\\varphi": "\U000003c6",
        "\\varrho": "\U000003c1",
        "\\vartheta": "\U000003b8",
        "\\vdash": "\U000022a2",
        "\\vee": "\U00002228",
        "\\wedge": "\U00002227",
        "\\Xi": "\U0000039e",
        "\\xi": "\U000003be",
        "\\yen": "\U000000a5",
        "\\zeta": "\U000003b6",
        )
        case = get_choice_opt(
        current_type = None
        current_value = None
        else:
        except TypeError:
        filter = NameHighlightFilter(
        Filter.__init__(self, **options)
        for name, default in [("spaces", "·"), ("tabs", "»"), ("newlines", "¶")]:
        for ttype, value in stream:
        if current_type is not None:
        if left < len(value):
        if name == filtername:
        if self.newlines:
        if self.tabs:
        if self.wstt:
        if start != last:
        if tokentype:
        lang = get_choice_opt(options, "lang", ["isabelle", "latex"], "isabelle")
        last = end
        left = n  # How many characters left to gobble.
        n = self.n
        raise ClassNotFound("filter %r not found" % filtername)
        regex = self.tag_re
        return cls(**options)
        return FILTERS[filtername]
        self.convert = getattr(str, case)
        self.exception = options.get("excclass", ErrorToken)
        self.n = get_int_opt(options, "n", 0)
        self.names = set(get_list_opt(options, "names", []))
        self.symbols = self.lang_map[lang]
        self.tag_re = re.compile(
        self.wstt = get_bool_opt(options, "wstokentype", True)
        start, end = match.start(), match.end()
        tabsize = get_int_opt(options, "tabsize", 8)
        tags = get_list_opt(
        tokentype = options.get("tokentype")
        try:
        yield name
        yield specialttype, replacefunc(value[start:end])
        yield ttype, value[last:]
       ``'latex'``.  The default is ``'isabelle'``.
       ``'upper'`` or ``'capitalize'``.  The default is ``'lower'``.
       A list of strings that are flagged as code tags.  The default is to
       highlight ``XXX``, ``TODO``, ``FIXME``, ``BUG`` and ``NOTE``.
       Now recognizes ``FIXME`` by default.
       The casing to convert keywords to. Must be one of ``'lower'``,
       The number of characters to gobble.
       The symbol language. Must be one of ``'isabelle'`` or
      (unicode PILCROW SIGN).  The default value is ``False``.
      (unicode RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK).  The default value
      `Name.Function`.
      A list of names that should be given the different token type.
      A token type or a string containing a token type name that is
      default is ``False``.
      disrupt background colors.  The default is ``True``.
      If it is another true value, spaces will be replaced by ``·`` (unicode
      If tabs are to be replaced by this filter (see the `tabs` option), this
      If this is a one-character string, spaces will be replaces by this string.
      If true, give whitespace the special `Whitespace` token type.  This allows
      is ``False``.  Note: this will not work if the `tabsize` option for the
      is the total number of characters that a tab should be expanded to.
      lexer is nonzero, as tabs will already have been expanded then.
      MIDDLE DOT).  If it is a false value, spaces will not be replaced.  The
      styling the visible whitespace differently (e.g. greyed out), but it can
      The default is ``8``.
      The default is `pygments.filters.ErrorToken`.
      The exception class to raise.
      The same as for `spaces`, but the default replacement character is ``»``
      The same as for `spaces`, but the default replacement character is ``¶``
      There is no default.
      used for highlighting the strings in `names`.  The default is
    """
    """Convert keywords to lowercase or uppercase or capitalize them, which
    """Convert mathematical symbols such as \\<longrightarrow> in Isabelle
    """Convert tabs, newlines and/or spaces to visible characters.
    """Gobbles source code lines (eats initial characters).
    """Highlight a normal Name (and Name.*) token with a different token type.
    """Highlight special code tags in comments and docstrings.
    """Lookup a filter by name. Return None if not found."""
    """Merges consecutive tokens with the same token type in the output
    """Raise an exception when the lexer generates an error token.
    """Return a generator of all filter names."""
    """Return an instantiated filter.
    "codetagify": CodeTagFilter,
    "gobble": GobbleFilter,
    "highlight": NameHighlightFilter,
    "keywordcase": KeywordCaseFilter,
    "raiseonerror": RaiseOnErrorTokenFilter,
    "symbols": SymbolFilter,
    "tokenmerge": TokenMergeFilter,
    "whitespace": VisibleWhitespaceFilter,
    .. versionadded:: 0.8
    .. versionadded:: 1.2
    .. versionchanged:: 2.13
    `case` : string
    `codetags` : list of strings
    `excclass` : Exception class
    `lang` : string
    `n` : int
    `names` : list of strings
    `newlines` : string or bool
    `spaces` : string or bool
    `tabs` : string or bool
    `tabsize` : int
    `tokentype` : TokenType or string
    `wstokentype` : bool
    }
    amount of space that isn't desired in the output.
    approximate the source rendering you'd see in an IDE.
    as functions. `Name.Function` is the default token type.
    ClassNotFound,
    cls = find_filter_class(filtername)
    code to your styleguide.
    Comment,
    def __init__(self, **options):
    def __init__(self, *args, **kwargs): pass
    def filter(self, lexer, stream):
    def gobble(self, value, left):
    else:
    Error,
    Example::
    for match in regex.finditer(value):
    for name, _ in find_plugin_filters():
    for name, cls in find_plugin_filters():
    get_bool_opt,
    get_choice_opt,
    get_int_opt,
    get_list_opt,
    if cls:
    if filtername in FILTERS:
    if last != len(value):
    isabelle_symbols = {
    Keyword,
    lang_map = {"isabelle": isabelle_symbols, "latex": latex_symbols}
    last = 0
    latex_symbols = {
    may be useful when the source code fed to the lexer is indented by a fixed
    means first letter uppercase, rest lowercase.
    Name,
    OptionError,
    Options accepted:
    Options are passed to the filter initializer if wanted.
    or \\longrightarrow in LaTeX into Unicode characters.
    Raise a ClassNotFound if not found.
    return None
    stream of a lexer.
    String,
    string_to_tokentype,
    This can be useful e.g. if you highlight Pascal code and want to adapt the
    This filter drops the first ``n`` characters off every line of code.  This
    This is mostly useful for HTML or console output when you want to
    This would highlight the names "foo", "bar" and "baz"
    Whitespace,
    yield from FILTERS
"""
)
:copyright: Copyright 2006-2023 by the Pygments team, see AUTHORS.
:license: BSD, see LICENSE for details.
}
~~~~~~~~~~~~~~~~
class CodeTagFilter:
class ErrorToken:
class GobbleFilter:
class KeywordCaseFilter:
class NameHighlightFilter:
class RaiseOnErrorTokenFilter:
class SymbolFilter:
class TokenMergeFilter:
class VisibleWhitespaceFilter:
def _replace_special(ttype, value, regex, specialttype, replacefunc=lambda x: x):
def find_filter_class(filtername):
def get_all_filters():
def get_filter_by_name(filtername, **options):
FILTERS = {
filters.
from pip._vendor.pygments.filter import Filter
from pip._vendor.pygments.plugin import find_plugin_filters
from pip._vendor.pygments.token import (
from pip._vendor.pygments.util import (
import re
Module containing filter lookup functions and default
pygments.filters

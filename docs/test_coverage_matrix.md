version: 1

modules:

&nbsp; - name: modules/log\_trace.py

&nbsp;   target: core

&nbsp;   functions:

&nbsp;     - name: get\_logger

&nbsp;       intent: logger 생성

&nbsp;       cases:

&nbsp;         normal:

&nbsp;           - id: basic

&nbsp;             input: { name: "log", level: "INFO" }

&nbsp;             expect: { type\_is: "Logger", name\_equals: "log" }



&nbsp; - name: modules/account\_runner.py

&nbsp;   target: core

&nbsp;   functions:

&nbsp;     - name: run\_all\_accounts

&nbsp;       intent: 계정 실행기

&nbsp;       cases:

&nbsp;         normal:

&nbsp;           - id: sample

&nbsp;             input: { accounts: \["a1"], timeout: 3 }

&nbsp;             expect: { returns\_contains: "done" }



&nbsp; - name: modules/pprint\_util\_custom.py

&nbsp;   target: core

&nbsp;   functions:

&nbsp;     - name: \_safe\_key

&nbsp;       intent: 키 필터링

&nbsp;       cases:

&nbsp;         normal:

&nbsp;           - id: filter

&nbsp;             input: { key: "k1" }

&nbsp;             expect: { returns\_contains: "k1" }

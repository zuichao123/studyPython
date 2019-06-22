# coding:utf-8
"""
sort
    以行为单位对文本进行排序。
    语法：
        sort [-b/d/f/g/i/M/n/r] [InFile]

    参数解释：
        -b: ignore-leading-blanks，忽略前面空格符部分

        -d: data-order，仅考虑空格和字母数字字符

        -f: ignore-case，忽略大小写

        -g: general-numeric-sort，根据一般数值进行排序

        -i: ignore-nonprinting，忽略不可打印的字符，比如换行符、回车符

        -M: month-sort，以月份进行排序

        -n: numeric-sort，根据字符串数值进行排序

        -r: reverse，反向输出排序结果

        -c: check，检查文本是否已排序，如果不是，则输出第一个乱序的行的相关信息，返回1

        -k N: key，以第N列进行排序

        -m S1 S2: merge，合并已排序的S1、S2文本，不再排序

        -o File: output，将结果写入File中

        -s: stable，通过禁用最后的比较来稳定排序
        -t sep: field-separator，使用sep作为分隔符来区分列
        -u: unique，去掉重复的行

        -z: 零终止的结束行，0字节，而不是换行符
"""
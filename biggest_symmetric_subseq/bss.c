//
//  main.c
//  c-tests
//
//  Created by anhtn on 8/26/16.
//  Copyright © 2016 anhtn. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

typedef unsigned int uint32;
typedef unsigned long ulong;

typedef struct {
    char *data;
    uint32 length;
} mystring;

int compare(const uint32 length1, const char *s1,
            const uint32 length2, const char *s2) {
    uint32 i;
    if (length1 != length2) return length1 - length2;
    for (i = 0; i < length1 / 2 + 1; i++) {
        int c = s1[i] - s2[i];
        if (c != 0) return c;
    }
    return 0;
}

void do_process(const char *s, const uint32 accept_zero,
                const uint32 from, const uint32 to,
                mystring** const cache, mystring* const result) {
    const uint32 size = to - from + 1;
    mystring sub, *c = &(cache[from][to]);
    uint32 i, j, last = from;
    char *tmp;

    if (from > to) {
        result->length = 0;
        return;
    } else if (from == to) {
        result->data = (char *)malloc(2);
        result->data[0] = s[from];
        result->data[1] = '\0';
        result->length = 1;
        return;
    } else if (c->length > 0) { // if exist in cache
        result->data = c->data;
        result->length = c->length;
        return;
    }

    result->data = (char *)malloc(size + 1);
    memset(result->data, '\0', size + 1);
    result->data[0] = '0';
    result->length = 1;

    tmp = (char *)malloc(size + 1);
    sub.length = 0;

    for (i = from; i <= to; i++) {
        if (result->length > to - i + 1) break;
        if (!accept_zero && s[i] == '0') continue;
        j = to + 1;
        while (--j > i && j > last) {
            if (s[i] != s[j]) continue;
            if (j > last) last = j;

            // calculate sub result
            do_process(s, 1, i + 1, j - 1, cache, &sub);

            // get tmp result
            memset(tmp, '\0', size);
            memcpy(tmp + 1, sub.data, sub.length);
            tmp[0] = s[j];
            tmp[sub.length + 1] = s[j];

            // if tmp result larger than current result
            if (compare(result->length, result->data, sub.length + 2, tmp) < 0) {
                memset(result->data, '\0', size);
                memcpy(result->data, tmp, sub.length + 2);
                result->length = sub.length + 2;
            }
        }
        if (result->length == 1 && s[i] > result->data[0]) {
            result->data[0] = s[i];
        }
    }

    // save to cache
    c->data = result->data;
    c->length = result->length;

    free(tmp);
}

void find_symmetric_substring(const uint32 size, const char* s) {
    uint32 i, j;
    mystring result;
    mystring **cache;

    cache = (mystring **)malloc(size * sizeof(mystring *));
    for (i = 0; i < size; i++) {
        cache[i] = (mystring *)malloc(size * sizeof(mystring));
        for (j = 0; j < size; j++) {
            cache[i][j].length = 0;
        }
    }
    result.length = 0;

    do_process(s, 0, 0, size - 1, cache, &result);
    printf("%s\n", result.data);

    for (i = 0; i < size; i++) {
        for (j = 0; j < size; j++) {
            if (cache[i][j].length) free(cache[i][j].data);
        }
        free(cache[i]);
    }
    free(cache);
}

ulong current_time_millis() {
    struct timeval tv;
    struct timezone tz;
    int ret = gettimeofday(&tv, &tz);
    if (ret) return 0;
    return tv.tv_sec*1000 + tv.tv_usec/1000;
}

void test(const char* s) {
    uint32 size = (uint32) strlen(s);

    ulong t1 = current_time_millis();
    find_symmetric_substring(size, s);

    ulong t2 = current_time_millis();
    printf("C _took:_%lu\n", (t2 - t1));
}

int main() {
    // int n;
    // char *s;
    // scanf("%d", &n);
    // s = (char *)malloc(n);
    // scanf("%s", s);
    //
    // find_symmetric_substring(n, s);
    //
    // free(s);

//     test("128921");
//     test("12312");
//     test("133122");
//     test("1352475813");
//     test("1352471358");
//     test("138247966");
//     test("17409");
//     test("13524713587788");
//     test("233288");
//     test("000008000");
//     test("0000");
//     test("002332880");
//     test("002339080632880");
//     test("48156358304135644341");
//     test("99422234716100521736232221412339904809850983058304853048580");
//     test("0942223471610052173623274071394593650269236430060759666590130421519169425831308408936440226597616819481539584598479005412539179370765803167001419075596848380732487806606361522984611439595084706077458769083051656319315355786856345643254110554824092938640375734174025600649225913371138668106870582977077921017620006238390856876916750398311503837396054441085698504158550428422326267611172087304264969997002016001432809752967860460879941899170242003487911668258685522492279951504444765129842298225004014343619644251050098996489443116992326916023366936812309011008674639457449804399147852956399494999571809871670582303608989462539455374284228057619155892282354221653116622120204048007966079076852703955211103559343942375230731006903270326419610166450262533479169352314706777202939500886091944494100620805908233026086710254562145989005787113190484188798634428895410756344871296449396311017427724723862149720148433505747680446320983518683236097642193903070743442497027664646236454593465967884115744785448444");
//    test(argv[0]);

//    printf("now1= %lu\n", current_time_millis());

    char s[1000], js[1000], msg[100];
    scanf("%s %s %s", s, js, msg);
    printf("%s\n", js);
    test(s);
    printf("%s\n", msg);

    return 0;
}

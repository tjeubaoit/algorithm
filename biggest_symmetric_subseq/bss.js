// author: tjeubaoit

function compare(s1, s2) {
  var n1 = s1.length;
  var n2 = s2.length;
  if (n1 != n2) return n1 - n2;
  for (var i = 0; i < n1 / 2 + 1; i++) {
    var c = s1[i] - s2[i];
    if (c !== 0) return c;
  }
  return 0;
}

function max(s1, s2) {
  return compare(s1, s2) >= 0 ? s1 : s2;
}

function doProcess_v2(s, acceptZero, fromIndex, toIndex, cache) {
  if (fromIndex == toIndex) return s[fromIndex];
  if (fromIndex > toIndex) return '';

  var i = 0;
  var result = cache[fromIndex][toIndex];
  if (result != undefined) return result;
  else result = '0';

  var last = fromIndex;
  for (i = fromIndex; i <= toIndex; i++) {
    if (result.length > toIndex - i + 1) break;
    if (!acceptZero && s[i] === '0') continue;
    var j = toIndex + 1;
    // last = Math.max(i, last);
    while (--j > last && j > i) {
      if (s[i] === s[j]) {
        // if (j - i + 1 == result.length && s[i] < result[0]) break;
        if (j > last) last = j;
        var sub = doProcess_v2(s, true, i + 1, j - 1, cache);
        var tmp = s[j] + sub + s[j];
        if (compare(result, tmp) < 0) result = tmp;
        break;
      }
    }
    if (result.length == 1 && s[i] > result) result = s[i];
  }

  cache[fromIndex][toIndex] = result;
  return result;
}

function doProcess_v4(s, acceptZero, i, j, cache, expectedSize) {
  if (i > j) return '';
  if (i == j) return s[i];

  var result = cache[i][j];
  if (result != undefined) {
    // console.log("found in cache: " + i + "," + j);
    return result;
  }

  if (!acceptZero && s[i] === '0') {
    var size = j - i;
    return expectedSize > size ? '' : doProcess_v4(s, acceptZero, i+1, j, cache, expectedSize);
  }

  if (s[i] === s[j]) {
    // console.log(i + "=" + j);
    var sub = doProcess_v4(s, true, i+1, j-1, cache, expectedSize - 2);
    result = s[i] + sub + s[j];
  } else {
    // console.log(i + "!=" + j);
    var size = j - i;
    if (expectedSize > size) {
      // console.log("ignore " + i + "," + j);
      return '';
    }
    var left = doProcess_v4(s, false, i, j-1, cache, expectedSize);
    // console.log("i=" + i + ", j=" + j + ", exptected=" + expectedSize + ", left=" + left);
    // if (left.length < expectedSize) { console.log("left size < exptected size"); return ''; }
    var right = doProcess_v4(s, false, i+1, j, cache, Math.max(left.length, expectedSize));
    result = max(left, right);
  }
  cache[i][j] = result;
  return result;
}

function findSymmetricSubstring(s) {
  var n = s.length;
  var x = new Array(n);
  for (var i = 0; i < n; i++) {
    x[i] = new Array(n);
  }
  // return doProcess_v3_lps(s, x);
  // return doProcess_v4(s, false, 0, n-1, x, 1);
  return doProcess_v2(s, false, 0, s.length - 1, x);
}

// process.stdin.resume();
// process.stdin.setEncoding('utf8');
// var input_string = '';
//
// process.stdin.on('data', function(chunk) {
//   input_string += chunk;
// });
//
// process.stdin.on('end', function() {
//   var lines = input_string.split('\n');
//   var s = lines[1];
//   console.log(findSymmetricSubstring(s))
// });

console.log(findSymmetricSubstring("128921"));
console.log(findSymmetricSubstring("12312"));
console.log(findSymmetricSubstring("133122"));
console.log(findSymmetricSubstring("1352475813"));
console.log(findSymmetricSubstring("1352471358"));
console.log(findSymmetricSubstring("138247966"));
console.log(findSymmetricSubstring("17409"));
console.log(findSymmetricSubstring("13524713587788"));
console.log(findSymmetricSubstring("233288"));
console.log(findSymmetricSubstring("000008000"));
console.log(findSymmetricSubstring("0000"));
console.log(findSymmetricSubstring("002332880"));
console.log(findSymmetricSubstring("002339080632880"));
console.log(findSymmetricSubstring("48156358304135644341"));
console.log(findSymmetricSubstring("2400472561"));
console.log(findSymmetricSubstring("25495298763"));

function makeRandomInput(size) {
  var text = "";
  var possible = "0123456789";
  for( var i = 0; i < size; i++ ) {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return text;
}

for (var i = 0; i < 1; i++) {
  // var input = "99422234716100521736232221412339904809850983058304853048580";
  var input = makeRandomInput(500);
  // console.log(input);
  var now = new Date().getTime();
  // if (!findSymmetricSubstring(input)) {
  //   console.log("fail: " + input);
  //   break;
  // } else console.log("true")
  // console.log(input);
  console.log(findSymmetricSubstring(input));
  console.log('JS_took:_' + (new Date().getTime() - now));
}

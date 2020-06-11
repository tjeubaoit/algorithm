# -*- coding: utf-8 -*-
# Dynamic Programming implementation of LCS problem


def lcs(X , Y):
    # find the length of the Strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    # return X[0:n-1]
    # return Y[0:m-1]
    return L[m][n]
#end of function lcs


def lcs1(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = ""
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    #lcs_set = ""
                    longest = c
                    lcs_set = S[i-c+1:i+1]
                elif c == longest:
                    lcs_set += S[i-c+1:i+1]

    return lcs_set
 
 
# Driver program to test the above function
test1 = "Nhà ở Thủ Đức còn dư 1phong trống cần cho thuê ở khu vực linh đông giá 1tr6 . + mình cần nữ thuê + diện + nước 150k /ng ( ko kèm tủ lạnh ... + phòng có ban công rộng rãi thoáng mát ,có cửa sổ . + nhà gần siêu thị ,chợ ,xe buýt đi mấy bước là tới . × Bn nào quan tâm liên hệ sdt 0933180556"
test2 = "[Nhà ở Thủ Đức còn dư 1phong trống cần cho thuê ở khu vực linh đông giá 1tr6 . + mình cần nữ thuê + diện + nước 150k /ng ( ko kèm tủ lạnh ... + phòng có ban công rộng rãi thoáng mát ,có cửa sổ . + nhà gần siêu thị ,chợ ,xe buýt đi mấy bước là tới . × Bn nào quan tâm liên hệ sdt 0933180556]"
test3 = "Nhà ở Thủ Đức còn dư 1phong trống cần cho thuê ở khu vực linh đông giá 1tr6 . + mình cần nữ thuê phòng + phòng có ban công rộng rãi thoáng mát ,có cửa sổ . + nhà gần siêu thị ,chợ ,xe buýt đi mấy bước là tới . × Bn nào quan tâm liên hệ sdt 0933180556"
test4 = "Nhà ở Thủ Đức còn dư 1phong trống cần cho thuê ở khu vực linh đông giá 1tr5 . + mình cần nữ thuê phòng + phòng có ban công rộng rãi thoáng mát ,có cửa sổ . + h giấc tự do . + nhà gần siêu thị ,chợ ,xe buýt đi mấy bước là tới . × Bn nào quan tâm liên hệ sdt 0933180556"
test5 = "Nhà mình ở Thủ Đức còn dư 1phong trống cần cho thuê ở khu vực linh đông giá 1tr6 . + mình cần nữ thuê + giờ giấc tự do ,cho nấu ăn trong phòng . + diện + nước 150k /ng ( ko kèm tủ lạnh ... + phòng có ban công rộng rãi thoáng mát ,có cửa sổ . + nhà gần siêu thị ,chợ ,xe buýt đi mấy bước là tới . × Bn nào quan tâm liên hệ sdt 0933180556"

r = lcs1(test1, test3)
print(len(test1))
print(r)
print(len(r)/float(len(test1)) * 100)

test6 = "Một phòng trong chung cư 335 Cầu Giấy ₫2,750,000 - Hà Nội Phòng 20m2, có điều hòa nóng lạnh, sàn gỗ. Cho thuê làm văn phòng hoặc ở. Điện nước theo giá nhà nước. sđth: 0981940359"
test7 = "Một phòng trong chung cư 335 Cầu Giấy ₫2,750,000 - Hà Nội Phòng 20m2, có điều hòa nóng lạnh, sàn gỗ. Cho thuê làm văn phòng hoặc ở. Điện nước theo giá nhà nước. 0981940359"
# print lcs1  (test6, test7)
r = lcs1(test6, test7)
print(r)
print(len(r)/float(len(test6)) * 100)

X = "22442"
Y = "44222"
print("Length of LCS is ", lcs(X, Y))
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_0

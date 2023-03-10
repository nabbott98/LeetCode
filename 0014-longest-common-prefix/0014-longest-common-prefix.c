char * longestCommonPrefix(char ** strs, int strsSize){
    if (strsSize == 0) return "";
    if (strsSize == 1) return strs[0];

    int len = 0, min = strlen(strs[0]);
    for (int i = 1; i < strsSize; ++i) {
        min = strlen(strs[i]) < min ? strlen(strs[i]) : min;
    }

    for (int c = 0; c < min; ++c) {
        for (int s = 0; s < strsSize - 1; ++s) {
            if (strs[s][c] == strs[s+1][c]) {
                if (s == strsSize - 2) {
                    ++len;
                }
            } else {
                goto br;
            }
        }
    }
    br:

    if (len > 0) {
        char* ret = malloc(len * sizeof(int));
        strs[0][len] = '\0';
        strcpy(ret, strs[0]);
        return ret;
    }

    return "";
}
class AB(object):
    def __init__(self, N=None, K=None):
        self.N=N
        self.K=K
        self.AB = ''
        
    def createString(self, N, K):
        if N <= 0:
            return ''
        elif N%2 == 1:
            self.max_Pairs = (N/2)*(N/2+1)
        elif N%2 == 0:
            self.max_Pairs = (N/2)**2
        
        if self.max_Pairs < K:
            return ''

        for ii in range(0,N):
            if ii < N/2:
                self.AB += 'B'
            else:
                self.AB += 'A'

        bs_on_right = 0
        fur_right_b = N/2-1
        next_b = N/2-2

        

        while (self.countPairs(self.AB) != K):
            temp_list = list(self.AB)
            temp_str = ''

            if (fur_right_b == N-1) or (temp_list[fur_right_b+1] == 'B'):
                fur_right_b = next_b
                next_b -= 1
            
            # print self.AB
            # print next_b, fur_right_b, N-1, temp_list[fur_right_b+1]

            temp_list[fur_right_b+1] = 'B'
            temp_list[fur_right_b] = 'A'
            fur_right_b += 1
            for jj in range(0,len(temp_list)):
                temp_str += temp_list[jj]
            self.AB = temp_str

            # print self.AB
            # print self.countPairs(self.AB)
            # print ''

        return self.AB


    def countPairs(self, string_AB):
        pair_Count = 0
        for ii in range(0,len(string_AB)):
            if string_AB[ii] == 'A':
                for jj in range(ii+1,len(string_AB)):
                    if string_AB[jj] == 'B':
                        pair_Count += 1
        return pair_Count

cc = AB()
print cc.createString(8,6)
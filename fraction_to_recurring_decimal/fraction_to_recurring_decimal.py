__author__ = 'daming'
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return ''
        if numerator == 0:
            return '0'

        ans = ""
        if numerator<0 and denominator>0 or numerator>0 and denominator<0:
            ans += "-"

        if numerator<0:
            numerator = -1*numerator
        if denominator<0:
            denominator = -1*denominator

        int_part =  numerator / denominator
        ans += str(int_part)

        remainder = numerator % denominator
        if remainder == 0:
            return ans
        ans += "."

        decimals = ""
        r_hash = {}
        cur_position = 0
        while remainder != 0:
            if remainder in r_hash:
                decimals = decimals[:r_hash[remainder]] + '(' + decimals[r_hash[remainder]:]
                decimals += ")"
                return ans + decimals
            r_hash[remainder] = cur_position
            remainder *= 10
            decimals += str(remainder/denominator)
            remainder = remainder%denominator
            cur_position += 1
        return ans + decimals

obj = Solution()
print obj.fractionToDecimal(1,6)



class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        Xtime = [0]*n
        fn_stack = []
        prev_time = 0
        for log in logs:
            fn, status, time = log.split(':')
            fn, time = int(fn), int(time)
            
            if status == 'start':
                if len(fn_stack) > 0:
                    Xtime[fn_stack[-1]] += (time - prev_time)
                fn_stack = fn_stack + [fn]
                prev_time = time
            else:
                Xtime[fn_stack.pop()] += (time - prev_time + 1)
                prev_time = time + 1
        
        return Xtime

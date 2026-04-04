class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        # Calculate the number of columns
        cols = len(encodedText) // rows
        
        decoded_chars = []
        
        # Iterate over every starting column in the top row
        for start_col in range(cols):
            r = 0
            c = start_col
            
            # Move diagonally down-right
            while r < rows and c < cols:
                # Map the 2D coordinates (r, c) to the 1D index
                index = r * cols + c
                decoded_chars.append(encodedText[index])
                
                # Move to the next diagonal cell
                r += 1
                c += 1
                
        # Join the characters and remove trailing spaces
        return "".join(decoded_chars).rstrip()
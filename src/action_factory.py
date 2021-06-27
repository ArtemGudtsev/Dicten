import action
import argument


def build_actions():
    return {
        #
        # analyse action - analyse text file to be encrypted
        #
        action.Action('analyse', 'Statistical analyse input file', {
            argument.Argument('input',
                              'Path to input file with text message',
                              has_param=True,
                              required=True)
        }),
        #
        # dict action - create dictionary file regarding specified parameters
        #
        action.Action('dict', 'Create encryption dictionary', {
            argument.Argument('byte-sequence-length',
                              'How many bytes will be in each sequence to replace 1 byte of message',
                              has_param=True,
                              required=False),
            argument.Argument('byte-sequence-count',
                              'How many sequences will be available for each byte',
                              has_param=True,
                              required=False),
            argument.Argument('output',
                              'Path to dictionary file to be created',
                              has_param=True,
                              required=True)
        }),
        #
        # encrypt action - encrypt text file with message
        #
        action.Action('encrypt', 'Encrypt text file with message, create new binary file as result', {
            argument.Argument('dictionary',
                              'Dictionary to be used for encryption',
                              has_param=True,
                              required=True),
            argument.Argument('use-noise',
                              'Flag to add true random bytes as noise to create more complexity for analysis',
                              has_param=False,
                              required=False),
            argument.Argument('noise-amount',
                              'Count of bytes in noise sequence',
                              has_param=True,
                              required=False),
            argument.Argument('input',
                              'Path to text file with message to be encrypted',
                              has_param=True,
                              required=True),
            argument.Argument('output',
                              'Path to binary file to be saved as result of encryption',
                              has_param=True,
                              required=True)
        }),
        #
        # decrypt action - decrypt binary file with secured message
        #
        action.Action('decrypt', 'Decrypt binary file to text message and save to file', {
            argument.Argument('dictionary',
                              'Dictionary to be used for decryption',
                              has_param=True,
                              required=True),
            argument.Argument('input',
                              'Path to binary file with encrypted message',
                              has_param=True,
                              required=True),
            argument.Argument('output',
                              'Path to text file to be created with text message encrypted',
                              has_param=True,
                              required=True)
        })
    }

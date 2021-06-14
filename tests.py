
class TestStringMethods(unittest.TestCase):

    def test_shannon(self):
        random_stringB64 = "ZWVTjPQSdhwRgl204Hc51YCsritMIzn8B=/p9UyeX7xu6KkAGqfm3FJ+oObLDNEva"
        random_stringHex = "b3A0a1FDfe86dcCE945B72" 
        self.assertGreater(truffleHog.shannon_entropy(random_stringB64, truffleHog.BASE64_CHARS), 4.5)
        self.assertGreater(truffleHog.shannon_entropy(random_stringHex, truffleHog.HEX_CHARS), 3)

    def test_cloning(self):
        project_path = truffleHog.clone_git_repo("https://github.com/dxa4481/truffleHog.git")
        license_file = os.path.join(project_path, "LICENSE")
        self.assertTrue(os.path.isfile(license_file))

    def test_unicode_expection(self):
        try:
            truffleHog.find_strings("https://github.com/dxa4481/tst.git")
        except UnicodeEncodeError:
            self.fail("Unicode print error")

    def test_return_correct_commit_hash(self):
        # Start at commit 202564cf776b402800a4aab8bb14fa4624888475, which 
        # is immediately followed by a secret inserting commit:
        # https://github.com/dxa4481/truffleHog/commit/d15627104d07846ac2914a976e8e347a663bbd9b
        since_commit = '202564cf776b402800a4aab8bb14fa4624888475'
        commit_w_secret = 'd15627104d07846ac2914a976e8e347a663bbd9b'
        cross_valdiating_commit_w_secret_comment = 'Oh no a secret file

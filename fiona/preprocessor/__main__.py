from fiona.preprocessor import TranslationPreprocessor


if __name__ == "__main__":
    processor = TranslationPreprocessor()
    processor.process('en_ja_jobs.csv', 'en', 'ja')

from steamship.data.corpus import CorpusImportRequest
from steamship.plugin.service import PluginRequest
from src.api import CorpusImporterPlugin
from steamship import MimeTypes

import os

__copyright__ = "Steamship"
__license__ = "MIT"


def test_corpus_importer():
    importer = CorpusImporterPlugin()

    request = PluginRequest(data=CorpusImportRequest())
    response = importer.run(request)

    assert(response.error is None)
    assert(response.data is not None)

    assert (response.data.fileImportRequests is not None)
    assert (len(response.data.fileImportRequests) == 2)

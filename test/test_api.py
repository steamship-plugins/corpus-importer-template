from steamship.plugin.corpus_importer import CorpusImportRequest
from steamship.plugin.service import PluginRequest
from src.api import CorpusImporterPlugin

import os

__copyright__ = "Steamship"
__license__ = "MIT"


def test_corpus_importer():
    importer = CorpusImporterPlugin()

    fileImportPlugin = "foo"

    request = PluginRequest(data=CorpusImportRequest(fileImporterPluginInstance=fileImportPlugin))
    response = importer.run(request)

    assert(response.error is None)
    assert(response.data is not None)

    assert (response.data.fileImportRequests is not None)
    assert (len(response.data.fileImportRequests) == 2)
    for req in response.data.fileImportRequests:
        assert(req.type == "fileImporter")
        assert(req.pluginInstance == fileImportPlugin)


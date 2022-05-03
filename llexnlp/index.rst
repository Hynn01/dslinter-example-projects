|Build Status| |Coverage Status| |image2| |Docs|

LexNLP by LexPredict
====================

Information retrieval and extraction for real, unstructured legal text
----------------------------------------------------------------------

LexNLP is a library for working with real, unstructured legal text,
including contracts, plans, policies, procedures, and other material.

LexNLP provides functionality such as:
--------------------------------------

-  Segmentation and tokenization, such as

   -  A sentence parser that is aware of common legal abbreviations like
      LLC. or F.3d.
   -  Pre-trained segmentation models for legal concepts such as pages
      or sections.

-  Pre-trained word embedding and topic models, broadly and for specific
   practice areas
-  Pre-trained classifiers for document type and clause type
-  Broad range of fact extraction, such as:

   -  Monetary amounts, non-monetary amounts, percentages, ratios
   -  Conditional statements and constraints, like "less than" or "later
      than"
   -  Dates, recurring dates, and durations
   -  Courts, regulations, and citations

-  Tools for building new clustering and classification methods
-  Hundreds of unit tests from real legal documents

.. figure:: https://s3.amazonaws.com/lexpredict.com-marketing/graphics/lexpredict_lexnlp_logo_horizontal_1.png
   :alt: Logo

Information
===========

-  ContraxSuite: https://contraxsuite.com/
-  LexPredict: https://lexpredict.com/
-  Official Website: https://lexnlp.com/
-  Documentation: http://lexpredict-lexnlp.readthedocs.io/en/latest/
   (in progress)
-  Contact: support@contraxsuite.com

Structure
---------

-  ContraxSuite web application:
   https://github.com/LexPredict/lexpredict-contraxsuite
-  LexNLP library for extraction:
   https://github.com/LexPredict/lexpredict-lexnlp
-  ContraxSuite pre-trained models and "knowledge sets":
   https://github.com/LexPredict/lexpredict-legal-dictionary
-  ContraxSuite agreement samples:
   https://github.com/LexPredict/lexpredict-contraxsuite-samples
-  ContraxSuite deployment automation:
   https://github.com/LexPredict/lexpredict-contraxsuite-deploy

Please note that ContraxSuite installations generally require trained models
or knowledge sets for usage.

Licensing
---------

LexNLP is available under a dual-licensing model. By default, this
library can be used under AGPLv3 terms as detailed in the repository
LICENSE file; however, organizations can request a release from the AGPL
terms or a non-GPL evaluation license by contacting ContraxSuite Licensing at
<license@contraxsuite.com>.

Requirements
------------

-  Python 3.6
-  see python-requirements.txt file for full information

Releases
--------

-  2.1.0: September 16, 2021 - Twenty third scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/2.1.0>`__
-  2.0.0: May 10, 2021 - Twenty second scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/2.0.0>`__
-  1.8.0: December 2, 2020 - Twenty first scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/1.8.0>`__
-  1.7.0: August 27, 2020 - Twentieth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/1.7.0>`__
-  1.6.0: May 27, 2020 - Nineteenth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/1.6.0>`__
-  1.4.0: December 20, 2019 - Eighteenth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/1.4.0>`__
-  1.3.0: November 1, 2019 - Seventeenth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/1.3.0>`__
-  0.2.7: August 1, 2019 - Sixteenth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.2.7>`__
-  0.2.6: June 12, 2019 - Fifteenth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.2.6>`__
-  0.2.5: March 1, 2019 - Fourteenth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.2.5>`__
-  0.2.4: February 1, 2019 - Thirteenth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.2.4>`__
-  0.2.3: Junuary 10, 2019 - Twelfth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.2.3>`__
-  0.2.2: September 30, 2018 - Eleventh scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.2.2>`__
-  0.2.1: August 24, 2018 - Tenth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.2.1>`__
-  0.2.0: August 1, 2018 - Ninth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.2.0>`__
-  0.1.9: July 1, 2018 - Ninth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.1.9>`__
-  0.1.8: May 1, 2018 - Eighth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.1.8>`__
-  0.1.7: April 1, 2018 - Seventh scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.1.7>`__
-  0.1.6: March 1, 2018 - Sixth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.1.6>`__
-  0.1.5: February 1, 2018 - Fifth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.1.5>`__
-  0.1.4: January 1, 2018 - Fourth scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.1.4>`__
-  0.1.3: December 1, 2017 - Third scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.1.3>`__
-  0.1.2: November 1, 2017 - Second scheduled public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.1.2>`__
-  0.1.1: October 2, 2017 - Bug fix release for 0.1.0;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.1.1>`__
-  0.1.0: September 30, 2017 - First public release;
   `code <https://github.com/LexPredict/lexpredict-lexnlp/tree/0.1.0>`__

.. |Build Status| image:: https://travis-ci.org/LexPredict/lexpredict-lexnlp.svg?branch=master
   :target: https://travis-ci.org/LexPredict/lexpredict-lexnlp
.. |Coverage Status| image:: https://coveralls.io/repos/github/LexPredict/lexpredict-lexnlp/badge.svg?branch=master
   :target: https://coveralls.io/github/LexPredict/lexpredict-lexnlp?branch=1.4.0
.. |image2| image:: https://tokei.rs/b1/github/lexpredict/lexpredict-lexnlp?category=code
   :target: https://github.com/lexpredict/lexpredict-lexnlp
.. |Docs| image:: https://readthedocs.org/projects/lexpredict-lexnlp/badge/?version=docs-1.4.0
   :target: http://lexpredict-lexnlp.readthedocs.io/en/docs-1.4.0/

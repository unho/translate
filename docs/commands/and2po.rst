
.. _and2po:
.. _po2and:

and2po
******

Converts Android String resource files to Gettext PO format.


.. _and2po#usage:

Usage
=====

.. code-block:: bash

  and2po [options] <android> <po>
  po2and [options] <po> <android>


Where:

+-----------+-----------------------------------------------------------------------+
| <android> | is a valid Android String Resource file or directory of those files   |
+-----------+-----------------------------------------------------------------------+
| <po>      | is a directory of PO or POT files                                     |
+-----------+-----------------------------------------------------------------------+

Options (and2po):

--version           show program's version number and exit
-h, --help          show this help message and exit
--manpage           output a manpage based on the help
--progress=PROGRESS
                    show progress as: :doc:`dots, none, bar, names, verbose
                    <option_progress>`
--errorlevel=ERRORLEVEL
                    show errorlevel as: :doc:`none, message, exception,
                    traceback <option_errorlevel>`
-i INPUT, --input=INPUT
                    read from INPUT in Android String Resource format
-x EXCLUDE, --exclude=EXCLUDE
                    exclude names matching EXCLUDE from input paths
-o OUTPUT, --output=OUTPUT
                    write to OUTPUT in po, pot formats
-t TEMPLATE, --template=TEMPLATE
                    read from TEMPLATE in Android String Resource format
-S, --timestamp
                    skip conversion if the output file has newer timestamp
-P, --pot           output PO Templates (.pot) rather than PO files (.po)
--duplicates=DUPLICATESTYLE
                    what to do with duplicate strings (identical source text):
                    :doc:`merge, msgctxt <option_duplicates>` (default:
                    'msgctxt')

Options (po2and):

--version           show program's version number and exit
-h, --help          show this help message and exit
--manpage           output a manpage based on the help
--progress=PROGRESS
                    show progress as: :doc:`dots, none, bar, names, verbose
                    <option_progress>`
--errorlevel=ERRORLEVEL
                    show errorlevel as: :doc:`none, message, exception,
                    traceback <option_errorlevel>`
-i INPUT, --input=INPUT
                    read from INPUT in po, pot formats
-x EXCLUDE, --exclude=EXCLUDE
                    exclude names matching EXCLUDE from input paths
-o OUTPUT, --output=OUTPUT
                    write to OUTPUT in Android String Resource format
-t TEMPLATE, --template=TEMPLATE
                    read from TEMPLATE in Android String Resource format
-S, --timestamp
                    skip conversion if the output file has newer timestamp
--threshold=PERCENT
                    only convert files where the translation completion is
                    above PERCENT
--fuzzy             use translations marked fuzzy
--nofuzzy           don't use translations marked fuzzy (default)


.. _and2po#format_coverage:

Formats coverage
================

Check :doc:`Android String Resource format </formats/android>` document to see
to which extent the Android String Resource format is supported.


.. _and2po#examples:

Examples
========
This example looks at roundtrip of Android String Resource translations as well
as recovery of existing translations.

First we need to create a set of POT files.


.. code-block:: bash

  and2po -P lang/en pot/


All .xml files found in the ``lang/en`` directory are converted to Gettext POT
files and placed in the ``pot`` directory.

If you are translating for the first time then you can skip the next step. If
you need to recover your existing translations then we do the following:


.. code-block:: bash

  and2po -t lang/en lang/zu po-zu/


Using the English Android String Resource files found in ``lang/en`` and your
existing Zulu translation in ``lang/zu`` we create a set of PO files in
``po-zu``. These will now have your translations. Please be aware that in order
for that to work 100% you need to have both English and Zulu at the same
revision, if they are not you will have to review all translations.

You are now in a position to translate your recovered translations or your new
POT files.

Once translated you can convert back as follows:


.. code-block:: bash

  po2and -t lang/en po-zu/ lang/zu


Your translations found in the Zulu PO directory, ``po-zu``, will be converted
to Android String Resources using the files in ``lang/en`` as templates and
placing your new translations in ``lang/zu``.

To update your translations simply redo the POT creation step and make use of
:doc:`pot2po` to bring your translation up-to-date.

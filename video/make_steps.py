"""Build the narrated video's steps (narrated-demo-video skill layout) from this run's screenshots and diagrams.

    python video/make_steps.py          # writes video/steps/NN-slug/{title.txt, shots.txt, narration.txt, *.png}

Narration is spelled for the Piper voice ("D B T", "sequel", "eye dempiere"); the video's subtitles spell
them back. Every number spoken is on screen in that step.
"""
import os, shutil

from PIL import Image
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHOTS, DIAG, CARDS = HERE / "shots", HERE / "diagrams", HERE / "cards"

STEPS = [
    ("01-intro", "EKOS on a legacy ERP: from analysis to reconciled marts", ["card:intro.png"],
     """This is a recording of one real run, start to finish. The source is eye dempiere, an open source E R P on Oracle,
     with nine hundred tables, twenty years of migration scripts and a large Java code base. We create a new project in
     the Ekos console and take it through the seven steps of the operator workflow. Analyse the sources. Generate the
     documentation. Review and sign off the source model. Describe the reports we want. Approve how each table is
     loaded. Build bronze and silver. And build the gold marts, each one reconciled against silver. Nothing here is
     staged: every screen is from this run, and every number we say is on screen. Where something went wrong during the
     recording, we say so, and we show how it was fixed."""),
    ("02-estate", "The estate: code and database", ["diagram:project-map.png", "diagram:source-er-keys.png"],
     """First, what we are dealing with. This map is how Ekos compiled the eye dempiere code base: the twenty largest
     path groups, from the base module with three thousand and eleven objects to the user interface and the migration
     scripts, linked by how often their files change together in the git history. The second picture is the part of the
     database this lakehouse is built for: the order to invoice slice, thirty three tables and their declared foreign
     keys, with orders, order lines, invoices and business partners highlighted. Both pictures are drawn from compiled
     facts, not by hand."""),
    ("03-analyse", "Step 1 — Analyse the sources",
     ["01-sources.png", "02-database-tested.png", "04-analysis-recover.png", "05-analysis-done.png",
      "06-census-equals-compiled.png", "07-dashboard.png"],
     """Step one. The Sources page holds the code checkout, the documentation site and the Oracle database, read through
     a read only account. Testing the connection reads the live catalog. Then one click: Init and compile. Ekos reads
     the code, the scripts, the documents and the catalog, and compiles them into one ledger, with no language model
     involved: the run page counts zero model calls. On this laptop the whole analysis took forty nine minutes, most of
     it the final commit, because the machine was swapping. Afterwards the census agrees with what was compiled: nine
     hundred and three tables, one hundred and sixty views and sixty two routines on both sides. The ledger now holds six
     hundred and seventy five thousand and thirty two entries."""),
    ("04-docs", "Step 2 — Documentation",
     ["08-docs-page.png", "11-docs-preview-run.png", "51-docs-published.png"],
     """Step two: documentation. Generate writes the estate as wiki pages, straight from the ledger: the data model by
     area, a page per table and routine, the schema history and the findings. No data value ever reaches a page. Preview
     publish shows what would change in the documentation store, here this repository's GitHub wiki, without sending
     anything. Once the review in step three narrowed the scope, the pages were generated again, two hundred and thirty
     nine of them, and published. The step bar now marks documentation as done."""),
    ("05-scope", "Step 3 — Review: scope",
     ["13-review-before.png", "14-scope-command.png", "15-scope-run.png", "16-scope-slice.png", "17-scope-signed.png"],
     """Step three is the review, and it is a person's job; here, a demo operator. Six subjects: scope, personal data,
     conflicts, identity, write behaviour and glossary. Scope first. Ekos proposed eight hundred and forty nine tables as
     business data. This lakehouse is for the order to invoice slice, so one command from the console puts the other
     eight hundred and sixteen tables out of scope, with a reason. The review now shows the slice. Signing off means
     typing the subject's name: the sign off is bound to a digest of exactly what was shown, and turns stale by itself if
     a fact behind it changes."""),
    ("06-conflicts", "Step 3 — Conflicts, identity and sign-off",
     ["18-conflict-decision.png", "19-conflict-recorded.png", "21-identity-decision.png", "22-pii.png",
      "23-review-signed.png"],
     """Inside the slice, seventeen conflicts block the sign off. Each one is a column the application's model calls
     mandatory, while the database allows null. Ekos keeps both claims, with their sources, and measures the data: here,
     zero contradicting rows. The operator decides that both are valid, and says why. One identity question remains: a
     git handle and a display name. The handle is the local part of that person's commit address, so they are the same
     contributor. Personal data, write behaviour and the glossary are signed as well. Six of six subjects signed: steps
     four to seven are no longer blocked."""),
    ("07-extraction", "Step 5 — The extraction plan",
     ["33-extraction-plan.png", "34-table-evidence-tile1.png", "35-change.png", "37-plan-approved.png"],
     """We continue with step five, not four, and that is a finding of this recording: requirements resolve against the
     deployed plan, so the plan has to be approved and generated first, even though the step bar suggests step four.
     The plan says, for each of the thirty three tables, how it lands in bronze. Incremental where the application's
     code keeps the updated column, full otherwise; how deletes are detected; which columns are masked. Every decision
     shows its evidence. The operator changes one table to a full load, with a reason, and approves the plan. Approval
     binds the plan's digest: nothing else can be generated."""),
    ("08-requirements", "Step 6 → Step 4 — Generate, then describe the marts",
     ["38-generate-run.png", "24-requirement-from-file.png", "25-draft-from-text.png", "27-draft-questions-tile3.png"],
     """Generate writes the pipeline: the extraction sequel, the D B T silver models with their tests, and the Dagster
     job. Now step four. Two marts are described as Markdown: sales by month and customer, and invoices by month. Every
     term resolves. The third is written in plain words: net sales of completed customer orders by month, product
     category and the customer's region. The local model, llama three, drafts the mart. This is the only language model
     call in the whole workflow, and Ekos does not trust it: it resolves every term against the approved model. Two
     terms fail. The measure is an expression the resolver does not accept, and the filter names a column that does not
     exist."""),
    ("09-answers", "Step 4 — The operator answers; nothing is invented",
     ["28-answer.png", "29-answered-tile3.png", "29-answered-tile4.png", "31-requirements-approved.png"],
     """Questions go to the operator, never back to the model. The operator replaces the measure with the sum of the
     order lines' net amount, and the filter with completed customer orders. Then Ekos asks a harder question: the
     customer's region can be reached from an order line along many different foreign key paths, each with a
     different meaning, and Ekos will not pick one. The operator names the path through the business partner's location. Every term now resolves,
     and the change log keeps each answer and who gave it. All three requirements are approved."""),
    ("10-load", "Step 6 — Bronze and silver through Dagster",
     ["40-run-launched.png", "41-dagster-1.png", "42-dagster-assets.png", "43-lakehouse-tables.png",
      "44-bar-after-load.png"],
     """Run the pipeline. Dagster loads the thirty three tables from Oracle into bronze, in Iceberg, and builds silver
     with D B T. The run succeeded: thirty six steps in five minutes and three seconds, sixty eight assets and eight
     hundred and ninety five checks. Getting here took three launches, and this is the second finding. The new project's
     silver first landed in the schema an earlier project uses, because silver and gold schema names ignored the
     project's prefix. We stopped, fixed the product so each project gets its own silver and gold schemas, regenerated
     and reloaded. Two tables carry data warnings: a document type and a payment type hold a code the application's
     code list does not declare."""),
    ("11-marts", "Step 7 — Marts: propose, merge, build, reconcile",
     ["45-mart-approved.png", "46-mart-proposed-tile3.png", "48-region_category_sales-reconciled-tile4.png",
      "48-region_category_sales-reconciled-tile5.png", "48-sales_by_month-reconciled-tile5.png", "49-marts.png"],
     """Step seven turns each approved requirement into a gold mart. Propose compiles the description into a D B T model
     on a branch, and checks that nothing in it was invented. Merge is the operator's approval. Build runs only that mart
     and its tests through Dagster. Reconcile reads each measure's total from the mart and computes the same total from
     silver. Every term is exact, and every total matches: three hundred and fifty eight point four zero for net sales by
     region and category, three hundred and seventy nine point nine zero and three orders for sales by month. All three
     marts are reconciled, in the project's own gold schema."""),
    ("12-lineage", "Models, transformations and lineage",
     ["55-dbt-lineage.png", "diagram:lineage-region_category_sales.png", "diagram:lineage-sales_by_month.png",
      "54-dbt-model.png"],
     """D B T's own lineage graph shows the models: bronze sources on the left, the silver models, and the three gold
     marts on the right. Column level lineage goes further. For net sales, the order line's net amount is cast into
     bronze, the latest version is kept in silver, and gold sums it. Month comes from the order date, truncated to the
     month. Every step is read from the generated sequel, not drawn by hand. Making this work for Oracle's upper case
     names was the third fix of this recording: the documentation tool matched names with their case."""),
    ("13-recap", "What we got", ["52-dashboard-final.png", "card:recap.png"],
     """To sum up. One new project, analysed from code, documents and the live database with zero model calls. Two
     hundred and thirty nine pages of documentation published. A review signed off by a person, decision by decision.
     Three marts described in Markdown or in plain words, resolved without invention, built through Dagster and reconciled to the cent. What
     is still open: two code values outside the application's lists in silver, the dashboard's growth chart timing out on
     this ledger, and the step bar suggesting requirements before the plan. Two product defects were found and fixed
     during the recording. Everything is in the repository, with the run log of this recording."""),
]


def fit(src, dst, size=(1920, 1080)):
    """Copy a shot; a picture of another shape (a diagram) is scaled into a white 16:9 frame, never stretched:
    the video scales every shot to 16:9."""
    im = Image.open(src)
    if im.size == size:
        shutil.copyfile(src, dst)
        return
    im = im.convert("RGB")
    im.thumbnail((int(size[0] * 0.88), int(size[1] * 0.88)), Image.LANCZOS)   # 6% a side: the video zooms and pans 4%
    frame = Image.new("RGB", size, "white")
    frame.paste(im, ((size[0] - im.width) // 2, (size[1] - im.height) // 2))
    frame.save(dst)


def main():
    root = HERE / "steps"
    root.mkdir(exist_ok=True)
    for sid, title, shots, text in STEPS:
        d = root / sid
        d.mkdir(exist_ok=True)
        (d / "title.txt").write_text(title + "\n")
        names = []
        for s in shots:
            kind, _, name = s.rpartition(":")
            src = {"diagram": DIAG, "card": CARDS}.get(kind, SHOTS) / name
            fit(src, d / name)
            names.append(name)
        (d / "badge.txt").write_text(f"{sid[:2].lstrip('0')} / {len(STEPS)}\n")
        (d / "shots.txt").write_text("\n".join(names) + "\n")
        (d / "narration.txt").write_text(" ".join(text.split()) + "\n")
        print(sid, len(names), "shots,", len(text.split()), "words")


if __name__ == "__main__":
    main()
